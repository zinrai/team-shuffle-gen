# team-shuffle-gen

team-shuffle-gen is a Python-based command-line tool that generates random groups from a list of names. It's perfect for need to randomly divide people into groups.

## Features

- Generates random groups from a list of names
- Allows customization of group size and number of groups to generate
- Ensures that the same name doesn't appear in consecutive outputs

## Usage

To use team-shuffle-gen, you need to provide a list of names via standard input and specify the group size and number of groups to generate.

Basic usage:

```bash
$ cat name-list.txt | ./team-shuffle-gen.py -g <group_size> -n <num_groups>
```

Options:
- `-g` or `--group_size`: Number of people in each group (required)
- `-n` or `--num_lines`: Number of groups to generate (required)

Example:

```bash
$ cat name-list.txt | ./team-shuffle-gen.py -g 2 -n 10
Sato , Shimizu
Kimura , Yamaguchi
Sasaki , Yoshida
Shimizu , Watanabe
Kobayashi , Saito
Yamamoto , Ito
Inoue , Kobayashi
Hayashi , Ito
Yamaguchi , Kimura
Matsumoto , Yamada
```

This command will create 5 groups, each containing 3 people, from the names listed in `name-list.txt`.

## Input Format

The input should be a text file with one name per line. For example:

```
Tanaka
Sato
Suzuki
Watanabe
Takahashi
Yamamoto
Nakamura
Kobayashi
Ito
Kato
Yoshida
Yamada
Sasaki
Yamaguchi
Saito
Matsumoto
Inoue
Kimura
Hayashi
Shimizu
...
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) for details.
