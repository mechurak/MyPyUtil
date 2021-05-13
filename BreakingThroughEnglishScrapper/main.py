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


def main():
    lectures = lecture_list.get_lecture_list(1)
    for lecture in lectures:
        video_url = get_video_url(lecture["lecture_id"])
        print(f'{lecture["title"]} | {lecture["date"]} | {video_url}')


if __name__ == "__main__":
    main()
