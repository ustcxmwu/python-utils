import os


def traverse_folder(target_folder, func):
    if not os.path.isdir(target_folder):
        return
    zh_vtt_files = []
    for root, dirs, files in os.walk(target_folder):
        for oneFile in files:
            candidate = os.path.join(root, oneFile)
            if os.path.isfile(candidate) and (candidate.find('zh-CN.vtt') or candidate.find('en.vtt') > 0):
                zh_vtt_files.append(candidate)
                func(candidate)
            elif os.path.isdir(candidate):
                sub_zh_vtt_files = traverse_folder(candidate, func)
                zh_vtt_files.extend(sub_zh_vtt_files)

    return zh_vtt_files


def vtt2srt(file_path):
    file_name, ext_name = os.path.splitext(file_path)
    if ext_name == ".vtt":
        print("Processing with file:    " + file_path)
        with open(file_path, "r", encoding="utf-8") as fin:
            content = fin.readlines()
            line_num = 2
            file_max_line_num = len(content)
            with open(file_name + ".srt", "w", encoding="utf-8") as fout:
                fout.write("1\n")
                for i in range(2, file_max_line_num):
                    fout.write(content[i].replace(".", ","))
                    if content[i].strip() == "" and i + 1 < file_max_line_num and content[i + 1].strip() != "":
                        fout.write(str(line_num) + "\n")
                        line_num += 1


if __name__ == '__main__':
    udacity = r'E:\utorrent_download\Udacity - Deep Reinforcement Learning (Nanodegree Program)'
    vtt_files = traverse_folder(udacity, vtt2srt)
    print(vtt_files)
