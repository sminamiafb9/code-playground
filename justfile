date := `date +%Y-%m-%d`

new lang topic try-out:
    direc="{{ lang }}/{{ topic }}/{{ date }}-{{ try-out }}" && \
    mkdir -p $direc && \
    echo "# {{ try-out }}" >> $direc/README.md
