import copy
import sys

from src.Util import syntaxHighlight, exo


def main():
    exo_json = exo.read(sys.argv[1])
    with open(sys.argv[2], "r", encoding="utf-8") as f:
        code = f.read()
    frame_per_character = 2  # 一文字あたりのフレーム数

    new_exo = [exo_json[0]]
    for i in range(len(code)):
        info_dict = copy.deepcopy(exo_json[1][0])
        # フレームは1始まりのため1を加算している
        info_dict["start"] = i * frame_per_character + 1
        info_dict["end"] = (i + 1) * frame_per_character

        obj_list = list()
        obj_detail_list = list()

        text_dict = copy.deepcopy(exo_json[1][1][0])
        cursor = "|" if i % 30 > 15 else ""
        highlight_code = syntaxHighlight.highlight(code[:i + 1]) + cursor
        text_dict["text"] = highlight_code.encode("utf-16").hex()[4:].ljust(4096, "0")

        obj_detail_list.append(text_dict)
        for j, detail in enumerate(exo_json[1][1]):
            if j == 0:
                continue
            obj_detail_list.append(exo_json[1][1][j])

        obj_list.append(info_dict)
        obj_list.append(obj_detail_list)
        new_exo.append(obj_list)

    exo.write(new_exo, r"../output/code.exo")


if __name__ == "__main__":
    main()
