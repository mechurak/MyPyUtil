import argparse

import requests

import lecture_list


def get_video_url(lecture_id: str) -> str:
    url = "https://home.ebse.co.kr/10mins_lee2/replay/3/ajax/getStreamUrl"

    data = {
        "lectId": lecture_id,
        "clsCd": "V06",
        "mode": "",
    }

    result = requests.post(url, data=data)
    info_dict = result.json()
    return info_dict["url"]


def main(the_args):
    print(the_args)
    target_page = the_args.page
    url_count = the_args.count

    lectures = lecture_list.get_lecture_list(target_page)
    target_lectures = reversed(lectures[:url_count])

    for lecture in target_lectures:
        video_url = get_video_url(lecture["lecture_id"])
        print(f'{lecture["title"]} | {lecture["date"]} | {video_url}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--page", default=1, help="target page number", type=int)
    parser.add_argument("-c", "--count", default=3, help="the number of videos to fetch url", type=int)

    args = parser.parse_args()
    main(args)
