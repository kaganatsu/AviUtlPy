import copy
import math
import sys

import pandas as pd

from src.Util import exo


def input_lyrics(path: str) -> list:
    df = pd.read_csv(path, encoding="utf-8", sep="\t", dtype={"lyric": str, "start": int, "end": int})
    return [v for v in df.to_dict("index").values()]


def main():
    exo_json = exo.read(sys.argv[1])
    lyrics = input_lyrics(sys.argv[2])
    rate = int(exo_json[0]["exedit"]["rate"])

    new_exo = [exo_json[0]]
    for i, lyric in enumerate(lyrics):
        info_dict = copy.deepcopy(exo_json[1][0])
        # フレームは1始まりのため1を加算している
        info_dict["start"] = math.floor(lyric["start"] / 1000 * rate) + 1
        info_dict["end"] = math.floor(lyric["end"] / 1000 * rate)

        obj_list = list()
        obj_detail_list = list()

        # テキストオブジェクトに歌詞を入力し設定する
        text_dict = copy.deepcopy(exo_json[1][1][0])
        text_dict["text"] = lyric["lyric"].encode("utf-16").hex()[4:].ljust(4096, "0")
        obj_detail_list.append(text_dict)
        # 入れ子のうち上で設定したテキストオブジェクト以外を設定する
        for j, detail in enumerate(exo_json[1][1]):
            if j == 0:
                continue
            obj_detail_list.append(exo_json[1][1][j])

        obj_list.append(info_dict)
        obj_list.append(obj_detail_list)
        new_exo.append(obj_list)

    exo.write(new_exo, r"../output/lyric.exo")


if __name__ == "__main__":
    main()
