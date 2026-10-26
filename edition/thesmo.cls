%% thesmo.cls — classe de l'édition des Thesmophories d'Aristophane
%% Composition par unités de quatre pages et plus, par folio du Ravennas :
%%   double page I  : transcription diplomatique de R (+ apparat, scholies, loci paralleli,
%%                    commentaire critique) | fac-similé du folio ;
%%   double page(s) II : texte grec établi | traduction, commentaire de la pièce au bas
%%                    des deux pages (deux colonnes par page).
%% Moteur : LuaLaTeX. Polices : EB Garamond (français), GFS Porson (grec établi),
%% Cardo (transcription diplomatique, scholies, signes métriques).
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{thesmo}[2026/10/25 v0.1 Edition des Thesmophories]
\LoadClass[twoside]{article}
\RequirePackage{iftex}
\RequireLuaTeX

%% ------------------------------------------------------------------ Géométrie
\RequirePackage[paperwidth=230mm, paperheight=310mm,
  inner=17mm, outer=11mm, top=17mm, bottom=16mm,
  headheight=4mm, headsep=5mm, footskip=8mm]{geometry}

%% ------------------------------------------------------------------ Polices
%% Les polices du dossier polices/ sont trouvées grâce à OSFONTDIR (voir compiler.sh).
\directlua{
  luaotfload.add_fallback("thesmofb", {"Cardo:mode=node;", "FreeSerif:mode=node;"})
}
\RequirePackage[french]{babel}
\babelprovide[import, onchar=ids fonts]{ancientgreek}
\babelfont{rm}[Extension=.otf, UprightFont=EBGaramond-Regular, ItalicFont=EBGaramond-Italic,
  BoldFont=EBGaramond-SemiBold, BoldItalicFont=EBGaramond-SemiBoldItalic,
  Numbers=OldStyle, RawFeature={fallback=thesmofb}]{EB Garamond}
\babelfont[ancientgreek]{rm}[Scale=0.93, RawFeature={fallback=thesmofb}]{GFS Porson}
%% La famille « sf » est détournée pour la transcription diplomatique :
%% latin en Garamond, grec en Cardo.
\babelfont{sf}[Extension=.otf, UprightFont=EBGaramond-Regular, ItalicFont=EBGaramond-Italic,
  BoldFont=EBGaramond-SemiBold, Numbers=OldStyle, RawFeature={fallback=thesmofb}]{EB Garamond}
\babelfont[ancientgreek]{sf}[Extension=.ttf, UprightFont=Cardo-Regular, ItalicFont=Cardo-Italic,
  BoldFont=Cardo-Bold, RawFeature={fallback=thesmofb}]{Cardo}
\newfontfamily\thesmo@metfont{Cardo}[Extension=.ttf, UprightFont=Cardo-Regular]
\newfontfamily\thesmo@grcaps{GFS Porson}[Scale=0.93, LetterSpace=12]
\newcommand\diplofont{\sffamily}
\newcommand\metfont{\thesmo@metfont}
\newcommand\petcap[1]{{\addfontfeature{Letters=SmallCaps, LetterSpace=6}#1}}
\newcommand\capsgr[1]{{\thesmo@grcaps #1}}
\frenchsetup{AutoSpacePunctuation=true}

%% ------------------------------------------------------------------ Couleurs
\RequirePackage{xcolor}
\RequirePackage{graphicx}
\definecolor{encre}{HTML}{161616}
\definecolor{gris}{HTML}{6E6E6E}
\definecolor{filet}{HTML}{9A9A9A}
%% Code couleur des mains du Ravennas (à ajuster après l'étude graphologique)
\definecolor{mainR1}{HTML}{161616}   % R1 : copiste du texte
\definecolor{mainR1c}{HTML}{6B5235}  % R1c : corrections du copiste lui-même
\definecolor{mainR2}{HTML}{A4161A}   % R2 : correcteur ancien
\definecolor{mainR3}{HTML}{7A3E9D}   % R3 : autre main ancienne
\definecolor{mainRsch}{HTML}{6B4E16} % main des scholies (si distincte de R1)
\definecolor{mainRrec}{HTML}{1D4E89} % Rrec : main récente (humaniste)
\definecolor{mainRmod}{HTML}{2D6A4F} % Rmod : main moderne (bibliothécaire…)
\definecolor{mainR?}{HTML}{707070}   % main non déterminée
\definecolor{rubrique}{HTML}{B5462B} % encre rouge du manuscrit
\definecolor{fondras}{HTML}{E9E4DA}  % fond des passages écrits sur grattage
\newcommand\main[2]{\textcolor{main#1}{#2}}

%% ------------------------------------------------------------------ Divers
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\newcommand\thesmo@hdL{}\newcommand\thesmo@hdR{}
\newcommand\entetes[2]{\gdef\thesmo@hdL{#1}\gdef\thesmo@hdR{#2}}
\fancyhead[LE,LO]{\footnotesize\color{gris}\thesmo@hdL}
\fancyhead[RE,RO]{\footnotesize\color{gris}\thesmo@hdR}
\fancyfoot[LE,RO]{\footnotesize\thepage}
\fancypagestyle{facsimile}{\fancyhf{}}
\RequirePackage{eso-pic}

%% ------------------------------------------------------------------ Moteur (expl3)
\ExplSyntaxOn
\newmarks \g_thesmo_item_marks

%% --- dimensions
\dim_new:N \l_thesmo_H_dim            % hauteur utile de page
\dim_new:N \l_thesmo_rowstrut_dim     % hauteur de la première ligne d'une rangée
\dim_new:N \l_thesmo_rowgap_dim       % espace entre rangées
\dim_new:N \l_thesmo_commsep_dim      % espace texte / commentaire
\dim_new:N \l_thesmo_commcol_dim      % largeur d'une colonne de commentaire
\dim_new:N \l_thesmo_commgap_dim      % gouttière entre colonnes
\dim_new:N \l_thesmo_commmin_dim      % hauteur minimale de la zone de commentaire
\dim_set:Nn \l_thesmo_rowgap_dim {0pt}
\dim_set:Nn \l_thesmo_commsep_dim {7mm}
\dim_set:Nn \l_thesmo_commgap_dim {7mm}
\dim_set:Nn \l_thesmo_commmin_dim {30mm}
\AtBeginDocument{ \dim_set:Nn \l_thesmo_commcol_dim { (\textwidth - \l_thesmo_commgap_dim) / 2 } \dim_set:Nn \l_thesmo_H_dim { \textheight } \thesmo_set_dwidths: }

%% --- paramètres typographiques (modifiables)
\tl_new:N \l_thesmo_grsize_tl  \tl_set:Nn \l_thesmo_grsize_tl {\fontsize{11}{15}\selectfont}
\tl_new:N \l_thesmo_frsize_tl  \tl_set:Nn \l_thesmo_frsize_tl {\fontsize{10.6}{15}\selectfont}
\tl_new:N \l_thesmo_commsize_tl \tl_set:Nn \l_thesmo_commsize_tl {\fontsize{8.6}{10.6}\selectfont}
\tl_new:N \l_thesmo_notesize_tl \tl_set:Nn \l_thesmo_notesize_tl {\fontsize{7.6}{9.4}\selectfont}

%% largeurs des colonnes des rangées
\dim_new:N \l_thesmo_spkG_dim \dim_set:Nn \l_thesmo_spkG_dim {15mm}
\dim_new:N \l_thesmo_spkF_dim \dim_set:Nn \l_thesmo_spkF_dim {29mm}
\dim_new:N \l_thesmo_num_dim  \dim_set:Nn \l_thesmo_num_dim {9mm}

%% --- état d'une section texte/traduction
\int_new:N \g_thesmo_rows_int
\int_new:N \g_thesmo_items_int
\box_new:N \g_thesmo_stream_box
\seq_new:N \g_thesmo_item_anchor_seq   % rangée d'ancrage de chaque article
\int_new:N \g_thesmo_lastverse_int
\tl_new:N \g_thesmo_section_gr_tl
\tl_new:N \g_thesmo_section_fr_tl
\seq_new:N \g_thesmo_row_verse_seq     % numéro de vers (ou vide) de chaque rangée
\seq_new:N \g_thesmo_row_secgr_seq
\seq_new:N \g_thesmo_row_secfr_seq

\cs_new_protected:Npn \thesmo_rowbox:nn #1#2 % #1 = G|F, #2 = index
  { g_thesmo_row #1 _ \int_eval:n {#2} _box }
\cs_new_protected:Npn \__thesmo_ensure_box:n #1
  { \box_if_exist:cF {#1} { \box_new:c {#1} } }

%% Rangée : #1 = boîte grecque (contenu horizontal complet), #2 = boîte française
\cs_new_protected:Npn \thesmo_add_row:nnn #1#2#3 % #3 = numéro de vers (affichage) ou vide
  {
    \int_gincr:N \g_thesmo_rows_int
    \tl_set:Nx \l_tmpa_tl { g_thesmo_rowG_ \int_use:N \g_thesmo_rows_int _box }
    \tl_set:Nx \l_tmpb_tl { g_thesmo_rowF_ \int_use:N \g_thesmo_rows_int _box }
    \__thesmo_ensure_box:n { \l_tmpa_tl }
    \__thesmo_ensure_box:n { \l_tmpb_tl }
    \vbox_gset_top:cn { \l_tmpa_tl } {#1}
    \vbox_gset_top:cn { \l_tmpb_tl } {#2}
    \seq_gput_right:Nx \g_thesmo_row_verse_seq {#3}
    \seq_gput_right:Nx \g_thesmo_row_secgr_seq { \exp_not:V \g_thesmo_section_gr_tl }
    \seq_gput_right:Nx \g_thesmo_row_secfr_seq { \exp_not:V \g_thesmo_section_fr_tl }
  }

%% Article de commentaire ancré à la rangée #1
\cs_new_protected:Npn \thesmo_add_item_at:nn #1#2
  {
    \int_gincr:N \g_thesmo_items_int
    \seq_gput_right:Nx \g_thesmo_item_anchor_seq { \int_max:nn {1} {#1} }
    \vbox_gset:Nn \g_thesmo_stream_box
      {
        \vbox_unpack_drop:N \g_thesmo_stream_box
        \hsize = \l_thesmo_commcol_dim
        \linewidth = \hsize
        \tex_marks:D \g_thesmo_item_marks { \int_use:N \g_thesmo_items_int }
        \l_thesmo_commsize_tl
        \parfillskip = 0pt plus 1fil
        \cs_set_eq:NN \\ \thesmo_safebreak
        #2
        \par
      }
  }
\cs_new_protected:Npn \thesmo_add_item:n #1
  { \thesmo_add_item_at:nn { \g_thesmo_rows_int } {#1} }
%% « \\ » tolérant dans le commentaire : saut de ligne en mode horizontal, rien ailleurs
\NewDocumentCommand \thesmo_safebreak { s o } { \mode_if_horizontal:T { \hfil \break } }
%% rangée où figure le vers #1 (premier nombre de l'étiquette) ; 0 si absent
\int_new:N \l_thesmo_anchorrow_int
\int_new:N \l_thesmo_target_int
\cs_new_protected:Npn \thesmo_row_of_verse:n #1
  {
    \thesmo_first_number:n {#1}
    \int_set_eq:NN \l_thesmo_target_int \l_thesmo_key_int
    \int_zero:N \l_thesmo_anchorrow_int
    \int_step_inline:nn { \seq_count:N \g_thesmo_row_verse_seq }
      {
        \int_compare:nNnT { \l_thesmo_anchorrow_int } = {0}
          {
            \tl_set:Nx \l_tmpa_tl { \seq_item:Nn \g_thesmo_row_verse_seq {##1} }
            \tl_if_empty:NF \l_tmpa_tl
              {
                \thesmo_first_number:V \l_tmpa_tl
                \int_compare:nNnF { \l_thesmo_key_int } < { \l_thesmo_target_int }
                  { \int_set:Nn \l_thesmo_anchorrow_int {##1} }
              }
          }
      }
  }

%% Test : avec une zone de commentaire de hauteur #1 (quatre colonnes),
%% quel est le dernier article commencé ? Résultat dans \l_thesmo_last_int ;
%% \l_thesmo_rest_bool = vrai si le flux n'est pas épuisé.
\int_new:N \l_thesmo_last_int
\bool_new:N \l_thesmo_rest_bool
\box_new:N \l_thesmo_tmp_box
\box_new:N \l_thesmo_part_box
\int_new:N \l_thesmo_done_items_int  % articles déjà commencés avant cette double page
\cs_new_protected:Npn \thesmo_test_split:n #1
  {
    \vbox_set:Nn \l_thesmo_tmp_box { \vbox_unpack:N \g_thesmo_stream_box }
    \int_set_eq:NN \l_thesmo_last_int \l_thesmo_done_items_int
    \prg_replicate:nn {4}
      {
        \box_if_empty:NF \l_thesmo_tmp_box
          {
            \vbox_set_split_to_ht:NNn \l_thesmo_part_box \l_thesmo_tmp_box {#1}
            \tl_set:Nx \l_tmpa_tl { \tex_splitbotmarks:D \g_thesmo_item_marks }
            \tl_if_empty:NF \l_tmpa_tl
              { \int_set:Nn \l_thesmo_last_int { \int_max:nn { \l_thesmo_last_int } { \l_tmpa_tl } } }
          }
      }
    \bool_set_false:N \l_thesmo_rest_bool
    \box_if_empty:NF \l_thesmo_tmp_box
      { \dim_compare:nNnT { \box_ht:N \l_thesmo_tmp_box + \box_dp:N \l_thesmo_tmp_box } > {0pt}
          { \bool_set_true:N \l_thesmo_rest_bool } }
  }

%% hauteur d'une rangée
\dim_new:N \l_thesmo_rowh_dim
\cs_new_protected:Npn \thesmo_row_height:n #1
  {
    \dim_set:Nn \l_thesmo_rowh_dim
      {
        \dim_max:nn
          { \box_ht:c { g_thesmo_rowG_ \int_eval:n {#1} _box } + \box_dp:c { g_thesmo_rowG_ \int_eval:n {#1} _box } }
          { \box_ht:c { g_thesmo_rowF_ \int_eval:n {#1} _box } + \box_dp:c { g_thesmo_rowF_ \int_eval:n {#1} _box } }
        + \l_thesmo_rowgap_dim
      }
  }

%% plus grand indice d'article ancré à une rangée <= #1
\int_new:N \l_thesmo_need_int
\cs_new_protected:Npn \thesmo_items_upto:n #1
  {
    \int_zero:N \l_thesmo_need_int
    \int_step_inline:nn { \seq_count:N \g_thesmo_item_anchor_seq }
      {
        \int_compare:nNnF { \seq_item:Nn \g_thesmo_item_anchor_seq {##1} } > {#1}
          { \int_set:Nn \l_thesmo_need_int {##1} }
      }
  }

%% Pagination de la section texte/traduction
\int_new:N \l_thesmo_a_int
\int_new:N \l_thesmo_b_int
\int_new:N \l_thesmo_best_int
\dim_new:N \l_thesmo_T_dim
\dim_new:N \l_thesmo_h_dim
\dim_new:N \l_thesmo_besth_dim
\bool_new:N \l_thesmo_go_bool
\bool_new:N \l_thesmo_streamleft_bool

\cs_new_protected:Npn \thesmo_stream_nonempty:
  {
    \bool_set_false:N \l_thesmo_streamleft_bool
    \box_if_empty:NF \g_thesmo_stream_box
      { \dim_compare:nNnT { \box_ht:N \g_thesmo_stream_box + \box_dp:N \g_thesmo_stream_box } > {0pt}
          { \bool_set_true:N \l_thesmo_streamleft_bool } }
  }

\cs_new_protected:Npn \thesmo_paginate:
  {
    \dim_set:Nn \l_thesmo_H_dim { \textheight }
    \int_set:Nn \l_thesmo_a_int {1}
    \int_zero:N \l_thesmo_done_items_int
    \thesmo_stream_nonempty:
    \bool_while_do:nn
      { \int_compare_p:nNn { \l_thesmo_a_int } > { \g_thesmo_rows_int } && \l_thesmo_streamleft_bool
        || \int_compare_p:nNn { \l_thesmo_a_int } < { \g_thesmo_rows_int + 1 } }
      {
        \int_set:Nn \l_thesmo_best_int { \l_thesmo_a_int - 1 }
        \dim_zero:N \l_thesmo_T_dim
        \int_set_eq:NN \l_thesmo_b_int \l_thesmo_a_int
        \bool_set_true:N \l_thesmo_go_bool
        \bool_while_do:nn
          { \l_thesmo_go_bool && \int_compare_p:nNn { \l_thesmo_b_int } < { \g_thesmo_rows_int + 1 } }
          {
            \thesmo_row_height:n { \l_thesmo_b_int }
            \dim_add:Nn \l_thesmo_T_dim { \l_thesmo_rowh_dim }
            \dim_set:Nn \l_thesmo_h_dim { \l_thesmo_H_dim - \l_thesmo_T_dim - \l_thesmo_commsep_dim }
            \thesmo_items_upto:n { \l_thesmo_b_int }
            \thesmo_stream_nonempty:
            \bool_if:NTF \l_thesmo_streamleft_bool
              {
                \dim_compare:nNnTF { \l_thesmo_h_dim } < { \l_thesmo_commmin_dim }
                  {
                    %% plus de place pour le commentaire : on accepte seulement si
                    %% aucun article n'attend (rare) ; sinon on s'arrête
                    \int_compare:nNnTF { \l_thesmo_need_int } > { \l_thesmo_done_items_int }
                      { \bool_set_false:N \l_thesmo_go_bool }
                      {
                        \dim_compare:nNnTF { \l_thesmo_T_dim } > { \l_thesmo_H_dim }
                          { \bool_set_false:N \l_thesmo_go_bool }
                          { \int_set_eq:NN \l_thesmo_best_int \l_thesmo_b_int }
                      }
                  }
                  {
                    \thesmo_test_split:n { \l_thesmo_h_dim }
                    \int_compare:nNnTF { \l_thesmo_need_int } > { \l_thesmo_last_int }
                      { \bool_set_false:N \l_thesmo_go_bool }
                      { \int_set_eq:NN \l_thesmo_best_int \l_thesmo_b_int }
                  }
              }
              {
                \dim_compare:nNnTF { \l_thesmo_T_dim } > { \l_thesmo_H_dim }
                  { \bool_set_false:N \l_thesmo_go_bool }
                  { \int_set_eq:NN \l_thesmo_best_int \l_thesmo_b_int }
              }
            \int_incr:N \l_thesmo_b_int
          }
        %% repli : au moins une rangée si des rangées restent
        \int_compare:nNnT { \l_thesmo_best_int } < { \l_thesmo_a_int }
          {
            \int_compare:nNnT { \l_thesmo_a_int } < { \g_thesmo_rows_int + 1 }
              { \int_set_eq:NN \l_thesmo_best_int \l_thesmo_a_int }
          }
        %% équilibrage : si toutes les rangées restantes tiennent mais que le commentaire
        %% déborde quand même, on garde la moitié des rangées pour la double page suivante
        \bool_lazy_and:nnT
          { \int_compare_p:nNn { \l_thesmo_best_int } = { \g_thesmo_rows_int } }
          { \int_compare_p:nNn { \l_thesmo_best_int - \l_thesmo_a_int } > {0} }
          {
            \dim_zero:N \l_thesmo_T_dim
            \int_step_inline:nnn { \l_thesmo_a_int } { \l_thesmo_best_int }
              { \thesmo_row_height:n {##1} \dim_add:Nn \l_thesmo_T_dim { \l_thesmo_rowh_dim } }
            \thesmo_stream_nonempty:
            \bool_if:NT \l_thesmo_streamleft_bool
              {
                \thesmo_test_split:n { \l_thesmo_H_dim - \l_thesmo_T_dim - \l_thesmo_commsep_dim }
                \bool_if:NT \l_thesmo_rest_bool
                  { \int_set:Nn \l_thesmo_best_int { \l_thesmo_a_int + \int_div_truncate:nn { \l_thesmo_best_int - \l_thesmo_a_int } {2} } }
              }
          }
        \thesmo_ship_spread:nn { \l_thesmo_a_int } { \l_thesmo_best_int }
        \int_set:Nn \l_thesmo_a_int { \l_thesmo_best_int + 1 }
        \thesmo_stream_nonempty:
      }
  }

%% Composition et sortie d'une double page : rangées #1..#2
\box_new:N \l_thesmo_left_box
\box_new:N \l_thesmo_right_box
\box_new:N \l_thesmo_c_box
\box_new:N \l_thesmo_cc_box
\box_new:N \l_thesmo_ccc_box
\box_new:N \l_thesmo_cccc_box
\dim_new:N \l_thesmo_lo_dim
\dim_new:N \l_thesmo_hi_dim
\dim_new:N \l_thesmo_mid_dim
\tl_new:N \l_thesmo_vfirst_tl
\tl_new:N \l_thesmo_vlast_tl

\cs_new_protected:Npn \thesmo_ship_spread:nn #1#2
  {
    %% hauteur du texte
    \dim_zero:N \l_thesmo_T_dim
    \int_compare:nNnF {#2} < {#1}
      {
        \int_step_inline:nnn {#1} {#2}
          { \thesmo_row_height:n {##1} \dim_add:Nn \l_thesmo_T_dim { \l_thesmo_rowh_dim } }
      }
    \dim_set:Nn \l_thesmo_h_dim { \l_thesmo_H_dim - \l_thesmo_T_dim - \l_thesmo_commsep_dim }
    \thesmo_stream_nonempty:
    \bool_if:NTF \l_thesmo_streamleft_bool
      {
        %% si tout le flux tient, on équilibre les quatre colonnes (recherche dichotomique)
        \thesmo_test_split:n { \l_thesmo_h_dim }
        \bool_if:NF \l_thesmo_rest_bool
          {
            \dim_zero:N \l_thesmo_lo_dim
            \dim_set_eq:NN \l_thesmo_hi_dim \l_thesmo_h_dim
            \prg_replicate:nn {14}
              {
                \dim_set:Nn \l_thesmo_mid_dim { (\l_thesmo_lo_dim + \l_thesmo_hi_dim) / 2 }
                \thesmo_test_split:n { \l_thesmo_mid_dim }
                \bool_if:NTF \l_thesmo_rest_bool
                  { \dim_set_eq:NN \l_thesmo_lo_dim \l_thesmo_mid_dim }
                  { \dim_set_eq:NN \l_thesmo_hi_dim \l_thesmo_mid_dim }
              }
            \dim_set:Nn \l_thesmo_h_dim { \l_thesmo_hi_dim + 0.5pt }
          }
        \vbox_set_split_to_ht:NNn \l_thesmo_c_box \g_thesmo_stream_box { \l_thesmo_h_dim }
        \__thesmo_note_marks:
        \vbox_set_split_to_ht:NNn \l_thesmo_cc_box \g_thesmo_stream_box { \l_thesmo_h_dim }
        \__thesmo_note_marks:
        \vbox_set_split_to_ht:NNn \l_thesmo_ccc_box \g_thesmo_stream_box { \l_thesmo_h_dim }
        \__thesmo_note_marks:
        \vbox_set_split_to_ht:NNn \l_thesmo_cccc_box \g_thesmo_stream_box { \l_thesmo_h_dim }
        \__thesmo_note_marks:
      }
      {
        \box_clear:N \l_thesmo_c_box \box_clear:N \l_thesmo_cc_box
        \box_clear:N \l_thesmo_ccc_box \box_clear:N \l_thesmo_cccc_box
        \dim_zero:N \l_thesmo_h_dim
      }
    %% en-têtes : section et bornes de vers
    \thesmo_spread_verses:nn {#1} {#2}
    \tl_set:Nx \l_tmpa_tl { \int_compare:nNnTF {#2} < {#1} { } { \seq_item:Nn \g_thesmo_row_secgr_seq {#1} } }
    \tl_set:Nx \l_tmpb_tl { \int_compare:nNnTF {#2} < {#1} { } { \seq_item:Nn \g_thesmo_row_secfr_seq {#1} } }
    %% page de gauche (grec)
    \thesmo_build_page:Nnnn \l_thesmo_left_box {G} {#1} {#2}
    \entetes { \exp_not:V \l_tmpa_tl } { \l_thesmo_vrange_tl }
    \thesmo_output_page:N \l_thesmo_left_box
    %% page de droite (traduction)
    \thesmo_build_page:Nnnn \l_thesmo_right_box {F} {#1} {#2}
    \entetes { \l_thesmo_vrange_tl } { \exp_not:V \l_tmpb_tl }
    \thesmo_output_page:N \l_thesmo_right_box
  }
\cs_new_protected:Npn \__thesmo_note_marks:
  {
    \tl_set:Nx \l_tmpa_tl { \tex_splitbotmarks:D \g_thesmo_item_marks }
    \tl_if_empty:NF \l_tmpa_tl
      { \int_set:Nn \l_thesmo_done_items_int { \int_max:nn { \l_thesmo_done_items_int } { \l_tmpa_tl } } }
  }

\tl_new:N \l_thesmo_vrange_tl
\cs_new_protected:Npn \thesmo_spread_verses:nn #1#2
  {
    \tl_clear:N \l_thesmo_vfirst_tl
    \tl_clear:N \l_thesmo_vlast_tl
    \int_compare:nNnF {#2} < {#1}
      {
        \int_step_inline:nnn {#1} {#2}
          {
            \tl_set:Nx \l_tmpa_tl { \seq_item:Nn \g_thesmo_row_verse_seq {##1} }
            \tl_if_empty:NF \l_tmpa_tl
              {
                \tl_if_empty:NT \l_thesmo_vfirst_tl { \tl_set_eq:NN \l_thesmo_vfirst_tl \l_tmpa_tl }
                \tl_set_eq:NN \l_thesmo_vlast_tl \l_tmpa_tl
              }
          }
      }
    \tl_if_empty:NTF \l_thesmo_vfirst_tl
      { \tl_clear:N \l_thesmo_vrange_tl }
      {
        \tl_if_eq:NNTF \l_thesmo_vfirst_tl \l_thesmo_vlast_tl
          { \tl_set:Nx \l_thesmo_vrange_tl { v.~\l_thesmo_vfirst_tl } }
          { \tl_set:Nx \l_thesmo_vrange_tl { vv.~\l_thesmo_vfirst_tl\,–\,\l_thesmo_vlast_tl } }
      }
  }

\cs_new_protected:Npn \thesmo_build_page:Nnnn #1#2#3#4 % boîte, G|F, a, b
  {
    \vbox_set_to_ht:Nnn #1 { \l_thesmo_H_dim }
      {
        \offinterlineskip
        \int_compare:nNnF {#4} < {#3}
          {
            \int_step_inline:nnn {#3} {#4}
              {
                \thesmo_row_height:n {##1}
                \vbox_to_ht:nn { \l_thesmo_rowh_dim }
                  { \box_use:c { g_thesmo_row #2 _ ##1 _box } \vss }
              }
          }
        \vfill
        \dim_compare:nNnT { \l_thesmo_h_dim } > {0pt}
          {
            %% filet de séparation (dans l'espace réservé \l_thesmo_commsep_dim)
            \hbox_to_wd:nn { \textwidth }
              { \str_if_eq:nnTF {#2} {G} { { \color{filet} \rule{0.22\textwidth}{0.35pt} } \hfil } { \hfil { \color{filet} \rule{0.22\textwidth}{0.35pt} } } }
            \skip_vertical:n { 2.6mm }
            \hbox_to_wd:nn { \textwidth }
              {
                \str_if_eq:nnTF {#2} {G}
                  { \box_use:N \l_thesmo_c_box \hfil \box_use:N \l_thesmo_cc_box }
                  { \box_use:N \l_thesmo_ccc_box \hfil \box_use:N \l_thesmo_cccc_box }
              }
          }
      }
  }

\cs_new_protected:Npn \thesmo_output_page:N #1
  {
    \par
    \noindent \box_use_drop:N #1
    \par \newpage
  }

%% ---------------------------------------------------------- Interface : texte et traduction
\NewDocumentEnvironment{texte}{}
  {
    \int_gzero:N \g_thesmo_rows_int
    \int_gzero:N \g_thesmo_items_int
    \seq_gclear:N \g_thesmo_item_anchor_seq
    \seq_gclear:N \g_thesmo_row_verse_seq
    \seq_gclear:N \g_thesmo_row_secgr_seq
    \seq_gclear:N \g_thesmo_row_secfr_seq
    \dim_set:Nn \l_thesmo_commcol_dim { (\textwidth - \l_thesmo_commgap_dim) / 2 }
    \box_gclear:N \g_thesmo_stream_box
    \thesmo_inject_continuation:
  }
  {
    \cleardoublepage@even
    \thesmo_paginate:
  }

%% vers : [numéro affiché]{personnage grec}{personnage français}{grec}{français}
%% options : n = numéro (affiché tous les 5, ou si force), cont = largeur d'antilabe,
%% met = schéma métrique, label = étiquette de mètre
\keys_define:nn { thesmo / vers }
  {
    n .tl_set:N = \l_thesmo_vn_tl,
    n .initial:n = {},
    indent .dim_set:N = \l_thesmo_vindent_dim,
    indent .initial:n = 0pt,
    findent .dim_set:N = \l_thesmo_findent_dim,
    findent .initial:n = 0pt,
    suite .bool_set:N = \l_thesmo_suite_bool,
    suite .default:n = true,
    suite .initial:n = false,
    met .tl_set:N = \l_thesmo_met_tl,
    met .initial:n = {},
    metre .tl_set:N = \l_thesmo_metre_tl,
    metre .initial:n = {},
    shownum .bool_set:N = \l_thesmo_shownum_bool,
    shownum .default:n = true,
    shownum .initial:n = false,
  }
\dim_new:N \g_thesmo_prevG_dim
\dim_new:N \g_thesmo_prevF_dim
\box_new:N \l_thesmo_meas_box

\tl_new:N \l_thesmo_numshow_tl

\NewDocumentCommand \vers { O{} m m m m }
  { \group_begin: \thesmo_vers:nnnnn {#1} {#2} {#3} {#4} {#5} \group_end: }
\cs_new_protected:Npn \thesmo_vers:nnnnn #1#2#3#4#5
  {
    \keys_set:nn { thesmo / vers } {#1}
    \bool_if:NT \l_thesmo_suite_bool
      {
        \dim_set:Nn \l_thesmo_vindent_dim { \g_thesmo_prevG_dim }
        \dim_set:Nn \l_thesmo_findent_dim { \g_thesmo_prevF_dim }
      }
    %% mesure des largeurs pour une éventuelle antilabè suivante
    \hbox_set:Nn \l_thesmo_meas_box { \l_thesmo_grsize_tl #4 }
    \dim_gset:Nn \g_thesmo_prevG_dim { \l_thesmo_vindent_dim + \box_wd:N \l_thesmo_meas_box + 0.6em }
    \hbox_set:Nn \l_thesmo_meas_box { \l_thesmo_frsize_tl #5 }
    \dim_gset:Nn \g_thesmo_prevF_dim
      { \dim_min:nn { \l_thesmo_findent_dim + \box_wd:N \l_thesmo_meas_box + 0.6em } { 0.42\textwidth } }
    \dim_gset:Nn \g_thesmo_prevG_dim { \dim_min:nn { \g_thesmo_prevG_dim } { 0.5\textwidth } }
    \tl_clear:N \l_thesmo_numshow_tl
    \bool_if:NTF \l_thesmo_shownum_bool
      { \tl_set_eq:NN \l_thesmo_numshow_tl \l_thesmo_vn_tl }
      {
        \regex_match:nVT { \A[0-9]+\Z } \l_thesmo_vn_tl
          {
            \int_compare:nNnT { \int_mod:nn { \l_thesmo_vn_tl } {5} } = {0}
              { \tl_set_eq:NN \l_thesmo_numshow_tl \l_thesmo_vn_tl }
          }
      }
    \thesmo_add_row:nnn
      {
        \hsize=\textwidth
        \l_thesmo_grsize_tl
        \noindent
        \hbox_to_wd:nn { \l_thesmo_spkG_dim } { \capsgr { \footnotesize #2 } \hfil }
        \hbox_overlap_left:n
          { \tl_if_empty:NF \l_thesmo_metre_tl { \footnotesize\itshape\color{gris} \l_thesmo_metre_tl \hspace{\l_thesmo_spkG_dim + 3mm} } }
        \vtop
          {
            \hsize = \dim_eval:n { \textwidth - \l_thesmo_spkG_dim - \l_thesmo_num_dim }
            \rightskip = 0pt plus 1fil
            \hangindent = 2em \hangafter = 1
            \noindent \strut \hspace*{\l_thesmo_vindent_dim} #4
            \tl_if_empty:NF \l_thesmo_met_tl
              { \hfill { \metfont \fontsize{8}{10}\selectfont \color{gris} \l_thesmo_met_tl } \hspace*{2mm} }
            \strut
          }
        \hbox_to_wd:nn { \l_thesmo_num_dim } { \hfil { \footnotesize \color{gris} \l_thesmo_numshow_tl } }
      }
      {
        \hsize=\textwidth
        \l_thesmo_frsize_tl
        \noindent
        \hbox_to_wd:nn { \l_thesmo_num_dim } { { \footnotesize \color{gris} \l_thesmo_numshow_tl } \hfil }
        \hbox_to_wd:nn { \l_thesmo_spkF_dim } { \hfil \petcap { \small #3 } \hspace{4mm} }
        \vtop
          {
            \hsize = \dim_eval:n { \textwidth - \l_thesmo_spkF_dim - \l_thesmo_num_dim }
            \rightskip = 0pt plus 1fil
            \hangindent = 1.5em \hangafter = 1
            \noindent \strut \hspace*{\l_thesmo_findent_dim} #5 \strut
          }
      }
      { \l_thesmo_vn_tl }
  }

%% rubrique de structure : {grec}{français}
\NewDocumentCommand \rubrique { m m }
  {
    \tl_gset:Nn \g_thesmo_section_gr_tl {#1}
    \tl_gset:Nn \g_thesmo_section_fr_tl {#2}
    \thesmo_add_row:nnn
      { \hsize=\textwidth \vbox_to_ht:nn {6mm}{} \centerline{ \capsgr{#1} } \vbox_to_ht:nn {4mm}{} }
      { \hsize=\textwidth \vbox_to_ht:nn {6mm}{} \centerline{ \addfontfeature{LetterSpace=12} \MakeUppercase{#2} } \vbox_to_ht:nn {4mm}{} }
      {}
  }
%% sous-rubrique (scène) : {grec ou vide}{français}
\NewDocumentCommand \scene { m m }
  {
    \thesmo_add_row:nnn
      { \hsize=\textwidth \vbox_to_ht:nn {3mm}{} \centerline{ \small #1 } \vbox_to_ht:nn {1.5mm}{} }
      { \hsize=\textwidth \vbox_to_ht:nn {3mm}{}
        \centerline{ \small\itshape #2 } \vbox_to_ht:nn {1.5mm}{} }
      {}
  }
%% didascalie (côté français)
\NewDocumentCommand \didascalie { m }
  {
    \thesmo_add_row:nnn
      { \hsize=\textwidth \strut }
      {
        \hsize=\textwidth
        \leftskip = \dim_eval:n { \l_thesmo_num_dim + \l_thesmo_spkF_dim } \relax
        \rightskip = 8mm plus 1fil
        \noindent { \fontsize{9.4}{12}\selectfont \itshape \strut #1 \strut }
      }
      {}
  }
%% espace entre unités
\NewDocumentCommand \blanc { O{3mm} }
  { \thesmo_add_row:nnn { \vbox_to_ht:nn {#1} {} } { \vbox_to_ht:nn {#1} {} } {} }

%% commentaire : {plage}{lemme}{texte} — ancré à la rangée du premier vers de la plage
\NewDocumentCommand \comm { m m +m }
  {
    \thesmo_row_of_verse:n {#1}
    \int_compare:nNnT { \l_thesmo_anchorrow_int } = {0}
      { \int_set_eq:NN \l_thesmo_anchorrow_int \g_thesmo_rows_int }
    \thesmo_add_item_at:nn { \l_thesmo_anchorrow_int }
      {
        \noindent
        \textbf{#1}\nobreakspace
        \tl_if_blank:nF {#2} { #2\,]\nobreakspace }
        #3
        \thesmo_flush_cnotes:
        \par \vspace{2.2pt}
      }
  }
%% notes de commentaire (appel + texte reporté à la fin de l'article)
\int_new:N \l_thesmo_cnote_int
\tl_new:N \l_thesmo_cnotes_tl
\NewDocumentCommand \nc { +m }
  {
    \int_incr:N \l_thesmo_cnote_int
    \textsuperscript{ \int_use:N \l_thesmo_cnote_int }
    \tl_put_right:Nx \l_thesmo_cnotes_tl
      { \exp_not:N \thesmo_cnote:nn { \int_use:N \l_thesmo_cnote_int } { \exp_not:n {#1} } }
  }
\cs_new_protected:Npn \thesmo_cnote:nn #1#2
  { \textsuperscript{#1}\,#2\space }
\cs_new_protected:Npn \thesmo_flush_cnotes:
  {
    \tl_if_empty:NF \l_thesmo_cnotes_tl
      {
        \par
        { \l_thesmo_notesize_tl \leftskip=1em \noindent \l_thesmo_cnotes_tl \par }
        \tl_clear:N \l_thesmo_cnotes_tl
      }
    \int_zero:N \l_thesmo_cnote_int
  }

%% ---------------------------------------------------------- Page diplomatique
%% Disposition : [scholies ancrées] [sigles | texte] [apparat ancré]
\dim_new:N \l_thesmo_dsch_dim  \dim_set:Nn \l_thesmo_dsch_dim {33mm}
\dim_new:N \l_thesmo_dsig_dim  \dim_set:Nn \l_thesmo_dsig_dim {8mm}
\dim_new:N \l_thesmo_dtxt_dim  \dim_set:Nn \l_thesmo_dtxt_dim {98mm}
\dim_new:N \l_thesmo_dapp_dim
\dim_new:N \l_thesmo_dgap_dim  \dim_set:Nn \l_thesmo_dgap_dim {3.5mm}
\dim_new:N \l_thesmo_dbs_dim   \dim_set:Nn \l_thesmo_dbs_dim {13.6pt}
\dim_new:N \l_thesmo_dvnum_dim \dim_set:Nn \l_thesmo_dvnum_dim {7mm}
\tl_new:N \l_thesmo_dsize_tl  \tl_set:Nn \l_thesmo_dsize_tl {\fontsize{9.4}{13.6}\selectfont}
\tl_new:N \l_thesmo_appsize_tl \tl_set:Nn \l_thesmo_appsize_tl {\fontsize{8}{9.6}\selectfont}
\tl_new:N \l_thesmo_schsize_tl \tl_set:Nn \l_thesmo_schsize_tl {\fontsize{6.8}{8.1}\selectfont}

\int_new:N \g_thesmo_dline_int
\seq_new:N \g_thesmo_dline_v_seq
\seq_new:N \g_thesmo_dline_n_seq
\seq_new:N \g_thesmo_app_seq
\seq_new:N \g_thesmo_sch_seq
\dim_new:N \l_thesmo_dln_dim \dim_set:Nn \l_thesmo_dln_dim {5mm}
\box_new:N \g_thesmo_dtext_box
\box_new:N \g_thesmo_dapp_box
\box_new:N \g_thesmo_dsch_box
\dim_new:N \g_thesmo_dapp_cur_dim
\dim_new:N \g_thesmo_dsch_cur_dim
\box_new:N \l_thesmo_entry_box
\box_new:N \g_thesmo_bottom_box
\box_new:N \g_thesmo_cont_box
\tl_new:N \g_thesmo_folio_tl
\tl_new:N \g_thesmo_fvv_tl
\tl_new:N \g_thesmo_fimage_tl

%% ancrage : place la boîte #3 dans la colonne #1 (app|sch) à la hauteur de la ligne #2
\cs_new_protected:Npn \thesmo_anchor_at:nnn #1#2#3
  {
    \vbox_set_top:Nn \l_thesmo_entry_box {#3}
    %% ligne de base visée = (n-1)*bs + strut
    \dim_set:Nn \l_tmpa_dim { \l_thesmo_dbs_dim * (#2 - 1) + 0.72\l_thesmo_dbs_dim - \box_ht:N \l_thesmo_entry_box }
    \dim_set:Nn \l_tmpb_dim { \use:c { g_thesmo_d #1 _cur_dim } }
    \dim_compare:nNnT { \l_tmpa_dim } < { \l_tmpb_dim } { \dim_set_eq:NN \l_tmpa_dim \l_tmpb_dim }
    \vbox_gset:cn { g_thesmo_d #1 _box }
      {
        \vbox_unpack_drop:c { g_thesmo_d #1 _box }
        \skip_vertical:n { \l_tmpa_dim - \l_tmpb_dim }
        \box_use:N \l_thesmo_entry_box
      }
    \dim_gset:cn { g_thesmo_d #1 _cur_dim }
      { \l_tmpa_dim + \box_ht:N \l_thesmo_entry_box + \box_dp:N \l_thesmo_entry_box + 1.6pt }
  }
%% numéro (premier nombre) d'une étiquette de vers : « 13-8 » → 13
\int_new:N \l_thesmo_key_int
\seq_new:N \l_thesmo_rx_seq
\cs_new_protected:Npn \thesmo_first_number:n #1
  {
    \regex_extract_once:nnNTF { \d+ } {#1} \l_thesmo_rx_seq
      { \int_set:Nn \l_thesmo_key_int { \seq_item:Nn \l_thesmo_rx_seq {1} } }
      { \int_set:Nn \l_thesmo_key_int {0} }
  }
\cs_generate_variant:Nn \thesmo_first_number:n { V }
%% indice de la ligne diplomatique où commence le vers #1 (0 si absent)
\int_new:N \l_thesmo_lineidx_int
\int_new:N \l_thesmo_cand_int
\cs_new_protected:Npn \thesmo_line_of_verse:n #1
  {
    \thesmo_first_number:n {#1}
    \int_set_eq:NN \l_thesmo_cand_int \l_thesmo_key_int
    \int_zero:N \l_thesmo_lineidx_int
    \int_step_inline:nn { \seq_count:N \g_thesmo_dline_v_seq }
      {
        \int_compare:nNnT { \l_thesmo_lineidx_int } = {0}
          {
            \tl_set:Nx \l_tmpa_tl { \seq_item:Nn \g_thesmo_dline_v_seq {##1} }
            \tl_if_empty:NF \l_tmpa_tl
              {
                \seq_set_split:NnV \l_tmpa_seq {,} \l_tmpa_tl
                \seq_map_inline:Nn \l_tmpa_seq
                  {
                    \thesmo_first_number:n {####1}
                    \int_compare:nNnT { \l_thesmo_key_int } = { \l_thesmo_cand_int }
                      { \int_set:Nn \l_thesmo_lineidx_int {##1} }
                  }
              }
          }
      }
  }
%% indice de la ligne diplomatique de numéro de ligne (manuscrit) #1
\cs_new_protected:Npn \thesmo_line_of_msline:n #1
  {
    \int_zero:N \l_thesmo_lineidx_int
    \int_step_inline:nn { \seq_count:N \g_thesmo_dline_n_seq }
      {
        \str_if_eq:eeT { \seq_item:Nn \g_thesmo_dline_n_seq {##1} } {#1}
          { \int_compare:nNnT { \l_thesmo_lineidx_int } = {0} { \int_set:Nn \l_thesmo_lineidx_int {##1} } }
      }
    \int_compare:nNnT { \l_thesmo_lineidx_int } = {0}
      { \regex_match:nnT { \A\d+\Z } {#1} { \int_set:Nn \l_thesmo_lineidx_int {#1} } }
  }

\NewDocumentEnvironment{folio}{ m m m }
  % #1 = folio (ex. 162v), #2 = vers (ex. 1–42), #3 = image du fac-similé
  {
    \tl_gset:Nn \g_thesmo_folio_tl {#1}
    \tl_gset:Nn \g_thesmo_fvv_tl {#2}
    \tl_gset:Nn \g_thesmo_fimage_tl {#3}
    \box_gclear:N \g_thesmo_cont_box
  }
  { }

\NewDocumentEnvironment{diplomatique}{ O{} }
  {
    \int_gzero:N \g_thesmo_dline_int
    \box_gclear:N \g_thesmo_dtext_box
    \box_gclear:N \g_thesmo_dapp_box
    \box_gclear:N \g_thesmo_dsch_box
    \dim_gzero:N \g_thesmo_dapp_cur_dim
    \dim_gzero:N \g_thesmo_dsch_cur_dim
    \seq_gclear:N \g_thesmo_dline_v_seq
    \seq_gclear:N \g_thesmo_dline_n_seq
    \thesmo_set_dwidths:
  }
  { }
\cs_new_protected:Npn \thesmo_set_dwidths:
  {
    \dim_gset:Nn \l_thesmo_dapp_dim
      { \textwidth - \l_thesmo_dsch_dim - \l_thesmo_dln_dim - \l_thesmo_dsig_dim - \l_thesmo_dtxt_dim - \l_thesmo_dvnum_dim - 2\l_thesmo_dgap_dim }
  }

%% \ligne[v=…, n=…, retrait=…]{sigles}{texte}
%%   v = vers qui commence sur la ligne (« 6 », ou « 6,7 ») ; n = numéro de ligne du manuscrit
\keys_define:nn { thesmo / ligne }
  {
    v .tl_set:N = \l_thesmo_lv_tl, v .initial:n = {},
    n .tl_set:N = \l_thesmo_ln_tl, n .initial:n = {},
    retrait .dim_set:N = \l_thesmo_lind_dim, retrait .initial:n = 0pt,
    echelle .tl_set:N = \l_thesmo_lscale_tl, echelle .initial:n = 1,
  }
\NewDocumentCommand \ligne { O{} m m }
  { \group_begin: \thesmo_ligne:nnn {#1} {#2} {#3} \group_end: }
\cs_new_protected:Npn \thesmo_ligne:nnn #1#2#3
  {
    \keys_set:nn { thesmo / ligne } {#1}
    \int_gincr:N \g_thesmo_dline_int
    \tl_if_empty:NT \l_thesmo_ln_tl { \tl_set:Nx \l_thesmo_ln_tl { \int_use:N \g_thesmo_dline_int } }
    \seq_gput_right:NV \g_thesmo_dline_v_seq \l_thesmo_lv_tl
    \seq_gput_right:NV \g_thesmo_dline_n_seq \l_thesmo_ln_tl
    \tl_clear:N \l_tmpb_tl
    \regex_match:nVT { \A\d+\Z } \l_thesmo_ln_tl
      { \int_compare:nNnT { \int_mod:nn { \l_thesmo_ln_tl } {5} } = {0} { \tl_set_eq:NN \l_tmpb_tl \l_thesmo_ln_tl } }
    \vbox_gset:Nn \g_thesmo_dtext_box
      {
        \vbox_unpack_drop:N \g_thesmo_dtext_box
        \hbox_to_wd:nn { \l_thesmo_dln_dim + \l_thesmo_dsig_dim + \l_thesmo_dtxt_dim + \l_thesmo_dvnum_dim }
          {
            \vbox_to_ht:nn { 0.72\l_thesmo_dbs_dim } { \vss }
            \hbox_to_wd:nn { \l_thesmo_dln_dim } { { \fontsize{5.5}{6}\selectfont \color{filet} \l_tmpb_tl } \hss }
            \hbox_to_wd:nn { \l_thesmo_dsig_dim } { \hss { \diplofont \fontsize{7.5}{9}\selectfont #2 } \hspace{1.5mm} }
            \hbox_set:Nn \l_thesmo_meas_box { \diplofont \l_thesmo_dsize_tl \hspace*{\l_thesmo_lind_dim} #3 }
            \hbox_to_wd:nn { \l_thesmo_dtxt_dim }
              {
                \dim_compare:nNnTF { \box_wd:N \l_thesmo_meas_box } > { \l_thesmo_dtxt_dim }
                  { %% ligne trop longue (tétramètres) : resserrement horizontal, au plus de 15 %
                    \box_scale:Nnn \l_thesmo_meas_box
                      { \fp_max:nn { 0.85 } { \dim_to_fp:n { \l_thesmo_dtxt_dim } / \dim_to_fp:n { \box_wd:N \l_thesmo_meas_box } } }
                      { 1 }
                    \box_use:N \l_thesmo_meas_box \hss }
                  { \box_use:N \l_thesmo_meas_box \hfil }
              }
            \hbox_to_wd:nn { \l_thesmo_dvnum_dim } { \hfil { \scriptsize \color{gris} \l_thesmo_lv_tl } }
            \vrule width 0pt depth 0.28\l_thesmo_dbs_dim
          }
      }
  }
%% apparat ancré au vers #1 ; scholie ancrée à la ligne #2 du manuscrit
\NewDocumentCommand \app { m +m }
  { \seq_gput_right:Nn \g_thesmo_app_seq { {#1} {#2} } }
\NewDocumentCommand \sch { O{} m +m }
  { \seq_gput_right:Nn \g_thesmo_sch_seq { {#2} {#1} {#3} } }
\seq_new:N \l_thesmo_place_seq
\cs_new_protected:Npn \thesmo_place_anchored:
  {
    %% apparat
    \seq_clear:N \l_thesmo_place_seq
    \seq_map_inline:Nn \g_thesmo_app_seq
      {
        \thesmo_line_of_verse:n { \use_i:nn ##1 }
        \int_compare:nNnT { \l_thesmo_lineidx_int } = {0}
          { \int_set:Nn \l_thesmo_lineidx_int { \int_max:nn {1} { \g_thesmo_dline_int } } }
        \seq_put_right:Nx \l_thesmo_place_seq
          { { \int_use:N \l_thesmo_lineidx_int } { \exp_not:o { \use_ii:nn ##1 } } }
      }
    \seq_sort:Nn \l_thesmo_place_seq
      {
        \int_compare:nNnTF { \use_i:nn ##1 } > { \use_i:nn ##2 }
          { \sort_return_swapped: } { \sort_return_same: }
      }
    \seq_map_inline:Nn \l_thesmo_place_seq
      {
        \thesmo_anchor_at:nnn {app} { \use_i:nn ##1 }
          { \hsize = \l_thesmo_dapp_dim \l_thesmo_appsize_tl \raggedright \hangindent=1em \hangafter=1
            \noindent \strut \use_ii:nn ##1 \strut }
      }
    %% scholies
    \seq_clear:N \l_thesmo_place_seq
    \seq_map_inline:Nn \g_thesmo_sch_seq
      {
        \thesmo_line_of_msline:n { \use_i:nnn ##1 }
        \int_compare:nNnT { \l_thesmo_lineidx_int } = {0} { \int_set:Nn \l_thesmo_lineidx_int {1} }
        \seq_put_right:Nx \l_thesmo_place_seq
          { { \int_use:N \l_thesmo_lineidx_int } { \exp_not:o { \use_ii:nnn ##1 } } { \exp_not:o { \use_iii:nnn ##1 } } }
      }
    \seq_sort:Nn \l_thesmo_place_seq
      {
        \int_compare:nNnTF { \use_i:nnn ##1 } > { \use_i:nnn ##2 }
          { \sort_return_swapped: } { \sort_return_same: }
      }
    \seq_map_inline:Nn \l_thesmo_place_seq
      {
        \thesmo_anchor_at:nnn {sch} { \use_i:nnn ##1 }
          { \hsize = \l_thesmo_dsch_dim \diplofont \l_thesmo_schsize_tl \raggedright \hangindent=0.6em \hangafter=1 \noindent
            \tl_if_blank:oF { \use_ii:nnn ##1 } { { \rmfamily\itshape\color{gris} \use_ii:nnn ##1 }\nobreakspace } \use_iii:nnn ##1 }
      }
    \seq_gclear:N \g_thesmo_app_seq
    \seq_gclear:N \g_thesmo_sch_seq
  }

%% registres du bas de la page diplomatique
\box_new:N \g_thesmo_par_box
\box_new:N \g_thesmo_crit_box
\tl_new:N \l_thesmo_bottomsize_tl \tl_set:Nn \l_thesmo_bottomsize_tl {\fontsize{8.2}{10.1}\selectfont}
\NewDocumentEnvironment{paralleles}{ +b }
  { \vbox_gset:Nn \g_thesmo_par_box
      { \hsize = \l_thesmo_commcol_dim \l_thesmo_bottomsize_tl \raggedright
        \noindent \petcap{loci~paralleli} \par \vspace{1pt} #1 \par } } {}
\NewDocumentEnvironment{critique}{ +b }
  { \vbox_gset:Nn \g_thesmo_crit_box
      { \hsize = \l_thesmo_commcol_dim \l_thesmo_bottomsize_tl
        \noindent \petcap{commentaire~critique} \par \vspace{1pt} #1 \par } } {}
\NewDocumentCommand \lp { m +m } { \noindent \textbf{#1}\nobreakspace #2 \par \vspace{1.5pt} }
\NewDocumentCommand \cc { m m +m }
  { \noindent \textbf{#1}\nobreakspace \tl_if_blank:nF {#2} { #2\,]\nobreakspace } #3 \par \vspace{2pt} }

%% composition et sortie de la double page diplomatique + fac-similé
\dim_new:N \l_thesmo_dtop_dim
\cs_new_protected:Npn \thesmo_ship_diplo:
  {
    \dim_set:Nn \l_thesmo_commcol_dim { (\textwidth - \l_thesmo_commgap_dim) / 2 }
    \thesmo_place_anchored:
    %% bloc supérieur
    \hbox_set:Nn \l_thesmo_left_box
      {
        %% chaque colonne commence par un filet de hauteur nulle : alignement par le haut
        \vbox_top:n { \hsize=\l_thesmo_dsch_dim \offinterlineskip \tex_hrule:D height 0pt \scan_stop: \vbox_unpack_drop:N \g_thesmo_dsch_box }
        \hspace{\l_thesmo_dgap_dim}
        \vbox_top:n { \hsize=\dim_eval:n { \l_thesmo_dln_dim + \l_thesmo_dsig_dim + \l_thesmo_dtxt_dim + \l_thesmo_dvnum_dim } \offinterlineskip \tex_hrule:D height 0pt \scan_stop: \vbox_unpack_drop:N \g_thesmo_dtext_box }
        \hspace{\l_thesmo_dgap_dim}
        \vbox_top:n { \hsize=\l_thesmo_dapp_dim \offinterlineskip \tex_hrule:D height 0pt \scan_stop: \vbox_unpack_drop:N \g_thesmo_dapp_box }
      }
    \dim_set:Nn \l_thesmo_dtop_dim { \box_ht:N \l_thesmo_left_box + \box_dp:N \l_thesmo_left_box }
    %% registres du bas : loci paralleli puis commentaire critique, en flux sur deux colonnes
    \vbox_set:Nn \l_thesmo_tmp_box
      {
        \box_if_empty:NF \g_thesmo_par_box { \vbox_unpack_drop:N \g_thesmo_par_box \vspace{4pt} }
        \box_if_empty:NF \g_thesmo_crit_box { \vbox_unpack_drop:N \g_thesmo_crit_box }
      }
    \dim_set:Nn \l_thesmo_h_dim { \l_thesmo_H_dim - \l_thesmo_dtop_dim - \l_thesmo_commsep_dim }
    \dim_set:Nn \l_tmpa_dim { \box_ht:N \l_thesmo_tmp_box + \box_dp:N \l_thesmo_tmp_box }
    \dim_compare:nNnTF { \l_tmpa_dim } < { 2\l_thesmo_h_dim }
      {
        %% équilibrage des deux colonnes
        \dim_set:Nn \l_thesmo_mid_dim { \l_tmpa_dim / 2 + 6pt }
        \vbox_set:Nn \l_thesmo_part_box { \vbox_unpack:N \l_thesmo_tmp_box }
        \vbox_set_split_to_ht:NNn \l_thesmo_c_box \l_thesmo_part_box { \l_thesmo_mid_dim }
        \vbox_set_split_to_ht:NNn \l_thesmo_cc_box \l_thesmo_part_box { \l_thesmo_mid_dim }
        \box_gclear:N \g_thesmo_cont_box
      }
      {
        \vbox_set_split_to_ht:NNn \l_thesmo_c_box \l_thesmo_tmp_box { \l_thesmo_h_dim }
        \vbox_set_split_to_ht:NNn \l_thesmo_cc_box \l_thesmo_tmp_box { \l_thesmo_h_dim }
        \vbox_gset:Nn \g_thesmo_cont_box { \vbox_unpack_drop:N \l_thesmo_tmp_box }
      }
    \cleardoublepage@even
    \entetes { \petcap{Codex~Ravennas~429}~·~f.~\g_thesmo_folio_tl } { \g_thesmo_fvv_tl }
    \noindent
    \vbox_to_ht:nn { \l_thesmo_H_dim }
      {
        \offinterlineskip
        \box_use_drop:N \l_thesmo_left_box
        \vfill
        \hbox_to_wd:nn { \textwidth } { \box_use_drop:N \l_thesmo_c_box \hfil \box_use_drop:N \l_thesmo_cc_box }
      }
    \par\newpage
    %% fac-similé
    \thispagestyle{facsimile}
    \AddToShipoutPictureFG*
      {
        \AtPageCenter
          {
            \makebox[0pt]
              { \raisebox{-0.5\height}
                { \includegraphics[height=\dim_eval:n { \paperheight - 16mm }, width=\dim_eval:n { \paperwidth - 14mm }, keepaspectratio]{ \g_thesmo_fimage_tl } } }
          }
        \put(\strip@pt\dimexpr\paperwidth-9mm\relax, 4mm)
          { \makebox[0pt][r]{ \fontsize{7}{8}\selectfont \color{gris} Ravenne,~Bibl.~Classense,~ms.~429,~f.~\g_thesmo_folio_tl \quad \thepage } }
      }
    \null\newpage
  }

\cs_new_protected:Npn \thesmo_inject_continuation:
  {
    \box_if_empty:NF \g_thesmo_cont_box
      {
        \thesmo_add_item:n
          {
            \noindent { \petcap{loci~paralleli~et~commentaire~critique}~(suite) } \par \vspace{1pt}
            \fontsize{8.2}{10.1}\selectfont \vbox_unpack_drop:N \g_thesmo_cont_box \par \vspace{4pt}
          }
      }
  }

%% fin des registres → sortie de la double page diplomatique
\NewDocumentCommand \finpagediplomatique {} { \thesmo_ship_diplo: }

%% page paire suivante
\cs_new_protected:Npn \cleardoublepage@even
  {
    \clearpage
    \int_if_odd:nT { \value{page} } { \null \thispagestyle{empty} \newpage }
  }
\ExplSyntaxOff

%% ------------------------------------------------------------------ Signes de transcription
%% Macros produites par outils/transcription/xml_vers_latex.py (voir ravennas/FORMAT_TRANSCRIPTION.md)
\RequirePackage{luacolor}
\RequirePackage{lua-ul}
\newcommand\Dcol[2]{\textcolor{main#1}{#2}}
\newcommand\Dpetit{\fontsize{5.8}{6}\selectfont}
\newcommand\Dnota[2][R1]{{\fontsize{7.5}{9}\selectfont\Dcol{#1}{#2}}\,}
\newcommand\Dparag{\rlap{\raisebox{-0.42\baselineskip}{\color{encre}\rule{4.2mm}{0.45pt}}}}
\newcommand\Dsupra[2]{\makebox[0pt][c]{\raisebox{1.32ex}[0pt][0pt]{\Dpetit\Dcol{#1}{#2}}}}
\newcommand\Dinfra[2]{\makebox[0pt][c]{\raisebox{-1.05ex}[0pt][0pt]{\Dpetit\Dcol{#1}{#2}}}}
\newcommand\Dadd[3][R1]{%
  \ifstrequal{#2}{dessus}{\Dsupra{#1}{#3}}{%
  \ifstrequal{#2}{dessous}{\Dinfra{#1}{#3}}{%
  \ifstrequal{#2}{ligne}{\Dcol{#1}{#3}}{%
  {\Dpetit\raisebox{0.6ex}{\color{gris}\textit{mg.}}}\,\Dcol{#1}{#3}}}}}
\newcommand\Ddel[3][R1]{%
  \ifstrequal{#2}{grattage}{{\color{gris}⟦}{\color{gris}\ifblank{#3}{\,·\,}{#3}}{\color{gris}⟧}}{%
  \ifstrequal{#2}{biffure}{\strikeThrough{#3}}{%
  \ifstrequal{#2}{exponctuation}{\Dcol{#1}{\underLine{#3}}}{%
  {\color{gris}#3}}}}}
\newcommand\Dsubst[3][R2]{\Dcol{#1}{#3}\ifblank{#2}{}{\textsuperscript{\Dpetit\color{gris}(#2)}}}
\newcommand\Dras[2][R1]{\highLight[fondras]{\Dcol{#1}{#2}}}
\newcommand\Dgap[1]{{\color{gris}[\,\foreach@dots{#1}\,]}}
\def\foreach@dots#1{\@tempcnta=#1\relax\loop\ifnum\@tempcnta>0 ·\advance\@tempcnta-1 \repeat}
\newcommand\Dabbr[2]{#1{\color{gris}(}#2{\color{gris})}}
\newcommand\Dgl[3][R1]{\setbox0\hbox{#2}\makebox[0pt][r]{\makebox[\wd0][c]{\raisebox{1.42ex}[0pt][0pt]{\Dpetit\Dcol{#1}{#3}}}}}
\newcommand\Dhi[2]{\ifstrequal{#1}{rouge}{\textcolor{rubrique}{#2}}{\ifstrequal{#1}{grand}{{\large #2}}{#2}}}
\newcommand\Dsp[1]{\hspace{#1\fontdimen2\font}\hspace{#1\fontdimen2\font}}
\newcommand\Dsigne[2]{{\fontsize{7.5}{9}\selectfont #2}}
\newcommand\Dzone[2]{\ifstrequal{#1}{titre}{\hfil #2\hfil}{\ifstrequal{#1}{hypothesis}{{\fontsize{8}{9}\selectfont #2}}{#2}}}
\newcommand\Dmain[2]{\Dcol{#1}{#2}}
\RequirePackage{etoolbox}
%% compatibilité avec la maquette d'essai
\newcommand\sig[1]{{\diplofont\fontsize{7.5}{9}\selectfont #1}}
\newcommand\supra[3][R2]{#2\Dsupra{#1}{#3}}
\newcommand\gl[3][R1]{#2\Dgl[#1]{#2}{#3}}
\newcommand\vv[1]{\textbf{#1}}
\newcommand\lem[1]{#1\,]}
\newcommand\om{\textit{om.}}
\newcommand\R{R}
\newcommand\Rac{R\textsuperscript{ac}}
\newcommand\Rpc{R\textsuperscript{pc}}
\newcommand\Rii{R\textsuperscript{2}}
\newcommand\Bibi{Bibi}
\newcommand\fol[2]{#1\textsuperscript{#2}}
\RequirePackage{thesmo-compat}
