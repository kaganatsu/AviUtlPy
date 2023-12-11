import configparser
import json
import re


def read(path: str) -> list:
    # exoファイルはini形式なのでConfigParserを使用する
    config = configparser.ConfigParser()
    config.read(path)
    # exoファイルはセクションの並びにも意味があるため、順番を維持するようにリストに格納する
    # config.sections()がセクションを順番通りに返す想定で以下の処理を記述している
    exo_list = []
    for section in config.sections():
        key = __section2key(section)
        if type(key) == str:
            exo_list.append({key: dict(config[section])})
            continue
        if type(key) == int:
            exo_list.append([dict(config[section]), []])
            continue
        if type(key) == tuple:
            # セクションが[0.0]という形式の場合、[0]の入れ子にして登録する
            exo_list[key[0] + 1][1].append(dict(config[section]))
    return exo_list


def __section2key(key: str):
    # セクションが[0]という形式の場合、intに変換する
    number = re.match(r"^\d+$", key)
    if number:
        return int(number.group(0))
    # セクションが[0.0]という形式の場合、一時的にtupleに変換する
    point_number = re.match(r"^(\d+)\.(\d+)$", key)
    if point_number:
        return int(point_number.group(1)), int(point_number.group(2))
    # 上記以外は文字列とする
    return key


def write(exo: list, path: str):
    ini = []
    for i, section in enumerate(exo):
        if type(section) == dict:
            for key, value in section.items():
                ini.append("[{0}]".format(str(key)))
                ini.extend(__ini(value))
            continue

        for inner_section in section:
            if type(inner_section) == dict:
                ini.append("[{0}]".format(i - 1))
                ini.extend(__ini(inner_section))
                continue

            for i2, inner_section2 in enumerate(inner_section):
                ini.append("[{0}.{1}]".format(i - 1, i2))
                ini.extend(__ini(inner_section2))

    config = configparser.ConfigParser()
    config.read_string("\n".join(ini))

    with open(path, "w", encoding="shift-jis") as f:
        config.write(f, space_around_delimiters=False)


def __ini(d: dict):
    ini = []
    for key, value in d.items():
        ini.append("{0}={1}".format(key, value))
    return ini


def main():
    d = read("../../sample/code/test.exo")
    with open("../../output/test.json", "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False)
    write(d, "../../sample/code/test.exo")


if __name__ == '__main__':
    main()
