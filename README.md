# code-playground

## Repository Structure

```sh
{lang}
    /{topic}
        /{yyyy-mm-dd}-{try-out}
            /README.md
            /{codes}.{ext}
```

- {lang}/{topic}ごとに依存ライブラリは管理。

```sh
just new {lang} {topic} {try-out}
```

justで生成するように設定している。
