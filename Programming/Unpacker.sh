#! /bin/sh -
PROGNAME="$0" exec tar -zxvvf - --to-command='
  case "$TAR_FILENAME" in
    (*.tar.gz | *.tgz) exec "$PROGNAME";;
    (*) set -o noclobber
        mkdir -p -- "$(dirname -- "$TAR_FILENAME")" &&
          exec cat > "$TAR_FILENAME"
  esac' 3<&-

# to use it gives it executable permissions and then run it like this: chmod +x Unpacker.sh && ./Unpacker.sh < file.tar.gz