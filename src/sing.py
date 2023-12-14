import copy
import math
import sys

import pandas as pd

from Util import exo


def input_lyrics(path: str) -> list:
    df = pd.read_csv(path, encoding="utf-8", sep="\t", dtype={"lyric": str, "start": int, "end": int})
    return [v for v in df.to_dict("index").values()]


def main():
    exo_json = exo.read(sys.argv[1])
    lyrics = input_lyrics(sys.argv[2])
    rate = int(exo_json[0]["exedit"]["rate"])
    vowel = ["あ", "い", "う", "え", "お", "ん"]

    new_exo = [exo_json[0]]
    for i, lyric in enumerate(lyrics):
        index = vowel.index(lyric["lyric"])
        info_dict = copy.deepcopy(exo_json[1][0])
        # フレームは1始まりのため1を加算している
        info_dict["start"] = math.floor(lyric["start"] / 1000 * rate) + 1
        info_dict["end"] = math.floor(lyric["end"] / 1000 * rate)
        info_dict["layer"] = 1

        obj_list = list()
        obj_detail_list = list()

        image_dict = copy.deepcopy(exo_json[index + 1][1][0])
        obj_detail_list.append(image_dict)
        for j, detail in enumerate(exo_json[1][1]):
            if j == 0:
                continue
            obj_detail_list.append(exo_json[1][1][j])

        obj_list.append(info_dict)
        obj_list.append(obj_detail_list)
        new_exo.append(obj_list)

    print(new_exo)
    exo.write(new_exo, r"../output/sing.exo")


if __name__ == "__main__":
    main()
