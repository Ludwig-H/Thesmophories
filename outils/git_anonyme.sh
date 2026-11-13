#!/bin/sh
# git avec l'identité anonyme du dépôt (CLAUDE.md, règle 1), quelles que soient les variables
# GIT_AUTHOR_* / GIT_COMMITTER_* injectées par l'environnement de travail.
# Usage : outils/git_anonyme.sh commit -m "…"   (ou toute autre commande git)
N="Ludwig-H"; E="158177790+Ludwig-H@users.noreply.github.com"
GIT_AUTHOR_NAME="$N" GIT_AUTHOR_EMAIL="$E" GIT_COMMITTER_NAME="$N" GIT_COMMITTER_EMAIL="$E" exec git "$@"
