# type: ignore
from typing import List, Union, Tuple, Any, Tuple, Dict, Optional, Sequence
import re
import pytube
import os
import re

import yt_dlp
import requests
from urllib.parse import urlparse, parse_qs
from .file_operations import create_missing_directory


import urllib.request


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



def download_list_of_youtube_videos(urls: list, directory: str, preferred_format: str="mp3", preferred_quality: str="192") -> List[Optional[Exception]]:
    errors: List[Optional[Exception]] = []
    if not os.path.exists(directory):
        os.makedirs(directory)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': preferred_format,
            'preferredquality': preferred_quality,
        }],
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                ydl.download([url])
                errors.append(None)
            except Exception as e:
                errors.append(e)

    return errors





def post_to_discord_webhook(
    message_content: str,
    webhook: str,
    name: str,
    avatar_url: Optional[str] = None,
    mention: bool = True,
    activate_voice: bool = False,
) -> Tuple[int, bytes]:
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




def extract_youtube_info(link: str) -> Dict[str, Union[str, dict, None]]:
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




def download_from_url_to_dir(url: str, dir: str, create: bool=True) -> bool:
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
    """
    r = requests.get(url)
    try:
        if create:
            create_missing_directory(dir)
        with open(dir + r.url.split("/")[-1], "wb", encoding="utf-8") as f:
            f.write(r.content)
        return True
    except:
        return False


def is_url_available(url: str, check_url: bool = True) -> Optional[bool]:
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
    except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
        return None


def get_all_videos_from_youtube_playlist(playlist_url: str) -> Union[List[str], Exception]:
    """
    Retrieves all video URLs from a YouTube playlist.

    Parameters:
    playlist_url (str): The URL of the YouTube playlist.

    Returns:
    Union[List[str], str]: A list of video URLs if successful, or an error message if an exception occurs.

    This function uses the PyTube library to extract video URLs from the provided playlist URL.
    In case of an error, the exception is returned as a string.
    """
    try:
        playlist = pytube.Playlist(playlist_url)
    
        video_links = playlist.video_urls
        
        return video_links
    
    except Exception as e:
        return e