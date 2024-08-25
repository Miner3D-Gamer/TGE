from typing import List, Union, Tuple, Any, Tuple, Dict, Optional
import re
import pytube
import os
import re
import pytube
import ffmpeg

import requests


import urllib.request
from .file_operations import make_legal_filename

def download_youtube_playlist(url: str, dir: str, quality:str, audio_type:str|None = None) -> None:
    """
    Downloads all the videos from a YouTube playlist and saves them to the specified directory.

    Args:
        url (str): The URL of the YouTube playlist.
        dir (str): The directory where the downloaded videos will be saved.
        create (bool): If True, creates the directory if it doesn't exist.

    Returns:
        None

    Raises:
        Any exceptions raised during the download and file write process are caught,
        and the function returns False if an exception occurs.

    Note:
        This function uses the 'pytube' library to download the videos. If 'create' is True, it creates the missing directory structure before saving the files.
    """

    playlist = pytube.Playlist(url)
    for video in playlist.videos:
        download_youtube_video(video.watch_url, dir, make_legal_filename(video.title), quality, audio_type)

def is_url(url: str) -> bool:
    """
    Check if a given string is a valid URL.

    This function uses regular expressions to determine whether the input string
    follows the typical pattern of a URL. It checks for patterns starting with
    'http://' or 'https://' followed by a valid domain name, and optional
    paths or query parameters.

    Args:
        url (str): The string to be checked as a potential URL.

    Returns:
        bool: True if the input string appears to be a valid URL, False otherwise.
    """
    pattern = re.compile(
        r"^(?:http|https)://"
        r"(?:[\w-]+\.)*[\w-]+"
        r"(?:\.[a-zA-Z]{2,})"
        r"(?:/?|(?:/[^\s]+)+)?$"
    )

    return bool(re.match(pattern, url))


def remove_html_tags(string: str) -> str:
    """
    Removes HTML tags from the given string.

    Args:
        string (str): The input string containing HTML tags.

    Returns:
        str: The modified string with HTML tags removed.

    Examples:
        >>> remove_html_tags('<p>Hello, <b>world!</b></p>')
        'Hello, world!'
        >>> remove_html_tags('<h1>Title</h1>')
        'Title'
    """
    return re.sub(r"<.*?>", "", string)


def get_youtube_video_id(input_string: str) -> str:
    """
    Extracts the YouTube video ID from a given string.

    This function supports various YouTube URL formats and directly provided video IDs.
    It returns an empty string if no valid video ID is found.

    Args:
        input_string (str): The input string containing a YouTube URL or video ID.

    Returns:
        str: The extracted YouTube video ID or an empty string if no ID is found.
    """
    video_id_pattern = r"^[a-zA-Z0-9_-]{11}$"

    url_patterns = [
        r"(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/|youtube\.com/v/)([a-zA-Z0-9_-]{11})",
        r"(?:https?://)?(?:www\.)?youtube\.com/.*[?&]v=([a-zA-Z0-9_-]{11})",
        r"(?:https?://)?(?:www\.)?youtube\.com/.*[&?]vi?=([a-zA-Z0-9_-]{11})",
    ]

    if re.match(video_id_pattern, input_string):
        return input_string

    for pattern in url_patterns:
        match = re.search(pattern, input_string)
        if match:
            return match.group(1)

    return ""




def is_internet_connected(
    max_timeout: int = 5, website: str = "https://www.google.com"
) -> bool:
    """
    The internet connectivity tester.

    Input:
        >>> max_timeout = int(seconds)
        >>> website = str("Website to test for")
    """
    try:
        urllib.request.urlopen(website, timeout=max_timeout)
        return True
    except Exception as e:
        return False



def download_youtube_video(
    url_or_id: str,
    save_path: str,
    file_name: str,
    quality: str,
    audio_type: Union[str, None] = None,
) -> Tuple[bool, str]:
    """
    Download a YouTube video as audio or video from the given URL and save it to the specified location.
    
    Args:
        url_or_id (str): The YouTube video URL or video ID. If a video ID is provided, it should be exactly 11 characters long.
        save_path (str): The directory path where the downloaded video will be saved.
        file_name (str): The desired name for the downloaded file. If no file extension is provided, '.mp4' or '.mp3' will be added.
        quality (str): Quality specification for video download. Can be 'audio', 'highest', 'lowest', or a specific resolution (e.g., '720p').
        audio_type (Union[str, None]): Audio file type to download ('mp4' or 'webm'). If `None`, defaults to 'mp4'.

    Returns:
        Tuple[bool, str]: A tuple containing a boolean indicating the success of the download (True for success, False for failure)
                        and a string describing the outcome.
    """
    id = get_youtube_video_id(url_or_id)
    if not re.search(r"\..+", file_name):
        file_extension = ".mp3" if quality == "audio" else ".mp4"
        file_name += file_extension

    try:
        yt = pytube.YouTube(id)
        if quality == "audio":
            if audio_type is None:
                audio_type = "mp4"
            audio_stream = yt.streams.filter(only_audio=True, file_extension=audio_type).first()
            audio_file_path = os.path.join(save_path, file_name)
            audio_stream.download(output_path=save_path, filename=file_name)

            # Convert audio to MP3 format using ffmpeg
            if audio_type != "mp3":
                mp3_file_path = os.path.splitext(audio_file_path)[0] + ".mp3"
                ffmpeg.input(audio_file_path).output(mp3_file_path).run()
                os.remove(audio_file_path)
                file_name = os.path.basename(mp3_file_path)

        elif quality == "highest":
            video = yt.streams.get_highest_resolution()
        elif quality == "lowest":
            video = yt.streams.get_lowest_resolution()
        else:
            video = yt.streams.get_by_resolution(quality)

        if quality != "audio":
            video.download(output_path=save_path, filename=file_name)

        return True, "Download successful"
    except Exception as e:
        return False, str(e)

def post_to_discord_webhook(
    message_content: str,
    webhook: str,
    name: str,
    avatar_url: str = None,
    mention: bool = True,
    activate_voice: bool = False,
) -> Any:
    """
    Posts a message to a Discord webhook. Returns the response code and the content of the message.
    """
    data = {
        "content": message_content, 
        "username": name,  
        "tts": activate_voice,  
        "allowed_mentions": {"parse": []} if mention else {},
    }
    if avatar_url is not None:
        data["avatar_url"] = avatar_url

    response = requests.post(webhook, json=data)
    return response.status_code, response.content


from urllib.parse import urlparse, parse_qs


def extract_youtube_info(link: str) -> Dict[str, Optional[str]]:
    """
    Extracts information from a YouTube video link.

    This function takes a YouTube video link as input and parses it to extract relevant information,
    including the video ID and other query parameters. The parsed information is returned as a dictionary.

    Args:
        link (str): The YouTube video link to be parsed.

    Returns:
        Dict[str, Optional[str]]: A dictionary containing extracted information.
            - 'video_id' (str): The unique ID of the YouTube video.
            - 'params' (dict): Other query parameters present in the URL, excluding the video ID.
                            The keys are parameter names, and the values are parameter values.

    Example:
        link = "https://www.youtube.com/watch?v=s7LS5lh0dLQ&feature=share"
        result = extract_youtube_info(link)
        # Result:
        # {
        #     'video_id': 's7LS5lh0dLQ',
        #     'params': {'feature': 'share'}
        # }
    """
    parsed_url = urlparse(link)
    query_params = parse_qs(parsed_url.query)
    if link.__contains__("/shorts/"):
        link = link.replace("/shorts/", "/watch?v=")

    video_id = query_params.get("v", [None])[0]

    other_params = {key: value[0] for key, value in query_params.items() if key != "v"}

    return {
        "video_id": video_id,
        "params": other_params,
    }


from .file_operations import create_missing_directory


def download_from_url_to_dir(url: str, dir: str, create: bool) -> None:
    """
    Downloads a file from the given URL and saves it to the specified directory.

    Args:
        url (str): The URL of the file to be downloaded.
        dir (str): The directory where the downloaded file will be saved.
        create (bool): If True, creates the directory if it doesn't exist.

    Returns:
        None

    Raises:
        Any exceptions raised during the download and file write process are caught,
        and the function returns False if an exception occurs.

    Note:
        This function uses the 'requests' library to download the file. If 'create' is
        set to True, it creates the missing directory structure before saving the file.
        The file is saved with the same name as the last part of the URL.

    Example:
        download_from_url_to_dir(
            'https://example.com/file.txt', '/path/to/directory/', create=True
        )
    """
    r = requests.get(url)
    try:
        if create:
            create_missing_directory(dir)
            with open(dir + r.url.split("/")[-1], "wb", encoding="utf-8") as f:
                f.write(r.content)
            return True
        else:
            with open(dir + r.url.split("/")[-1], "wb", encoding="utf-8") as f:
                f.write(r.content)
            return True
    except:
        return False


def is_url_available(url: str, check_url: bool = True) -> bool:
    """
    Check the availability of a URL by sending a GET request and evaluating the response status code.

    Parameters:
    url (str): The URL to be checked for availability.
    check_url (bool, optional): If True, performs a basic URL format check before proceeding (default: True).

    Returns:
    bool: True if the URL is available and returns a status code of 200, False otherwise.
    """
    if check_url:
        check_url = not is_url(url)

    if not check_url:
        return False

    try:
        r = requests.get(url)
        if r.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:
        return None


def get_youtube_playlist_links(playlist_url):
    try:
        # Create a Playlist object using the URL
        playlist = pytube.Playlist(playlist_url)
        
        # Fetch all video URLs in the playlist
        video_links = playlist.video_urls
        
        return video_links
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []