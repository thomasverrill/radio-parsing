import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import matplotlib.pyplot as plt
from collections import Counter

#  variable to store the Spinitron URL

urls = {
    "thoge": "https://playlists.wprb.com/WPRB/dj/173612/thoge?layout=1&page=1",
    "Abe": "https://playlists.wprb.com/WPRB/dj/172622/Abe?layout=1&page=1",
    "Navi": "https://playlists.wprb.com/WPRB/dj/169885/Navi?layout=1&page=1",
    "Jon Solomon": "https://playlists.wprb.com/WPRB/show/206059/Jon-Solomon?layout=1&page=1",
    "chef pat": "https://playlists.wprb.com/WPRB/dj/172629/chef-pat?layout=1&page=1",
    "Rosasolis Dream": "https://playlists.wprb.com/WPRB/dj/152911/rosasolis-dream?layout=1&page=1",
    "rena": "https://playlists.wprb.com/WPRB/dj/172623/rena?layout=1&page=1",
    "DJ Scheki": "https://playlists.wprb.com/WPRB/dj/181173/DJ-Scheki?layout=1&page=1",
    "Number 6": "https://playlists.wprb.com/WPRB/dj/149855/Number-6?layout=1&page=1",
    "John Weingart": "https://playlists.wprb.com/WPRB/dj/149737/John-Weingart?layout=1&page=1",
    "DJ Rat Princess": "https://playlists.wprb.com/WPRB/dj/177564/DJ-Rat-Princess?layout=1&page=1",
    "DJ Ringworm": "https://playlists.wprb.com/WPRB/dj/160547/DJ-Ringworm?layout=1&page=1",
    "Phil Jackson": "https://playlists.wprb.com/WPRB/dj/150833/Phil-Jackson?layout=1&page=1",
    "K Train": "https://playlists.wprb.com/WPRB/dj/184716/K-Train?layout=1&page=1",
    "Jen": "https://playlists.wprb.com/WPRB/dj/149435/Jen?layout=1&page=1",
    "evanescent": "https://playlists.wprb.com/WPRB/dj/184707/evanescent?layout=1&page=1",
    "DJ Mirey": "https://playlists.wprb.com/WPRB/dj/181187/DJ-Mirey?layout=1&page=1",
    "DJ Joppa Fallston": "https://playlists.wprb.com/WPRB/dj/181168/DJ-Joppa-Fallston?layout=1&page=1",
    "DJ Jupiter": "https://playlists.wprb.com/WPRB/dj/180004/DJ-Jupiter?layout=1&page=1",
    "Esoterica": "https://playlists.wprb.com/WPRB/dj/149843/Esoterica?layout=1&page=1",
    "DJ Bohr": "https://playlists.wprb.com/WPRB/dj/181172/DJ-Bohr?layout=1&page=1",
    "Charles xcx": "https://playlists.wprb.com/WPRB/dj/184692/Charles-xcx?layout=1&page=1",
    "Krista": "https://playlists.wprb.com/WPRB/dj/149458/Krista?layout=1&page=1",
    "a.i.r.": "https://playlists.wprb.com/WPRB/dj/184708/a-i-r?layout=1&page=1",
    "Bia": "https://playlists.wprb.com/WPRB/dj/177561/Bia?layout=1&page=1",
    "Dan Ruccia": "https://playlists.wprb.com/WPRB/dj/149560/Dan-Ruccia?layout=1&page=1",
    "Wilbo": "https://playlists.wprb.com/WPRB/dj/162119/Wilbo?layout=1&page=1",
    "Lili": "https://playlists.wprb.com/WPRB/dj/148762/Lili?layout=1&page=1",
    "Lizbot": "https://playlists.wprb.com/WPRB/dj/149600/Lizbot?layout=1&page=1",
    "DJ Sheff": "https://playlists.wprb.com/WPRB/dj/177560/DJ-Sheff?layout=1&page=1",
    "TB": "https://playlists.wprb.com/WPRB/dj/149603/TB?layout=1&page=1",
    "Quinneth": "https://playlists.wprb.com/WPRB/dj/167484/Quinneth?layout=1&page=1",
    "DJ Sharke": "https://playlists.wprb.com/WPRB/dj/184709/DJ-Sharke?layout=1&page=1",
    "Marvin Rosen": "https://playlists.wprb.com/WPRB/dj/149609/Marvin-Rosen?layout=1&page=1",
    "Dan Buskirk": "https://playlists.wprb.com/WPRB/dj/149870/Dan-Buskirk?layout=1&page=1",
    "Methuselah Mouse": "https://playlists.wprb.com/WPRB/dj/160550/Methuselah-Mouse?layout=1&page=1",
    "DJ Slæyer": "https://playlists.wprb.com/WPRB/dj/172618/DJ-Sl%C3%A6yer?layout=1&page=1",
    "Bani": "https://playlists.wprb.com/WPRB/dj/160556/Bani?layout=1&page=1",
    "crispy cookie": "https://playlists.wprb.com/WPRB/dj/172620/crispy-cookie?layout=1&page=1",
    "Momo": "https://playlists.wprb.com/WPRB/dj/185383/Momo?layout=1&page=1",
    "Aid Hempson": "https://playlists.wprb.com/WPRB/dj/184706/Aid-Hempson?layout=1&page=1",
    "Agent Emi": "https://playlists.wprb.com/WPRB/dj/184711/Agent-Emi?layout=1&page=1",
    "Krista": "https://playlists.wprb.com/WPRB/dj/149458/Krista?layout=1&page=1",
    "DJ Toomis": "https://playlists.wprb.com/WPRB/dj/179041/DJ-Toomis?layout=1&page=1",
    "Cynthia": "https://playlists.wprb.com/WPRB/dj/177558/Cynthia?layout=1&page=1",
    "DJ Brodius": "https://playlists.wprb.com/WPRB/dj/180002/DJ-Brodius?layout=1&page=1",
    "sophia": "https://playlists.wprb.com/WPRB/dj/177562/sophia?layout=1&page=1",
    "DJ LDP": "https://playlists.wprb.com/WPRB/dj/184712/DJ-LDP?layout=1&page=1",
    "ǝɹnɔsqꓳ ǝɥꓕ ǝʌɐꓷ": "https://playlists.wprb.com/WPRB/dj/149579/%C7%9D%C9%B9n%C9%94sq%EA%93%B3-%C7%9D%C9%A5%EA%93%95-%C7%9D%CA%8C%C9%90%EA%93%B7?layout=1&page=1",
    "DJ Senni Kat": "https://playlists.wprb.com/WPRB/dj/179942/DJ-Senni-Kat?layout=1&page=1",
    "Jerry Gordon": "https://playlists.wprb.com/WPRB/dj/149621/Jerry-Gordon?layout=1&page=1",
    "Readie Righteous": "https://playlists.wprb.com/WPRB/dj/149615/Readie-Righteous?layout=1&page=1",
    "Dana K": "https://playlists.wprb.com/WPRB/dj/149576/Dana-K?layout=1&page=1",
    "Mike Hunter": "https://playlists.wprb.com/WPRB/dj/149876/Mike-Hunter?layout=1&page=1",
    "DJ Aneek": "https://playlists.wprb.com/WPRB/dj/184713/DJ-Aneek?layout=1&page=1",
    "MJ": "https://playlists.wprb.com/WPRB/dj/184714/MJ?layout=1&page=1",
    "Sangeet Team": "https://playlists.wprb.com/WPRB/dj/149585/Sangeet-Team-Dave-Jayashri-Ramaprasad-Rungun-Padma?layout=1&page=1",
    "Fankie": "https://playlists.wprb.com/WPRB/dj/169852/Fankie?layout=1&page=1",
    "DJ DebbieWebby": "https://playlists.wprb.com/WPRB/dj/173678/DJ-DebbieWebby?layout=1&page=1",
    "DJ Mackerel": "https://playlists.wprb.com/WPRB/dj/181169/DJ-Mackerel?layout=1&page=1",
    "Commie Francis": "https://playlists.wprb.com/WPRB/dj/149438/Commie-Francis?layout=1&page=1",
    "the CZAR": "https://playlists.wprb.com/WPRB/dj/181167/the-CZAR?layout=1&page=1",
    "lina": "https://playlists.wprb.com/WPRB/dj/172624/lina?layout=1&page=1",
    "DJ Catemoji": "https://playlists.wprb.com/WPRB/dj/184715/DJ-Catemoji?layout=1&page=1",
    "DJ NEM": "https://playlists.wprb.com/WPRB/dj/160512/DJ-NEM?layout=1&page=1",
}
url_keys = list(urls.keys())
dj_rhcounts = {}
# "" :  "?layout=1&page=1",
test_playlist_url = (
    "https://playlists.wprb.com/WPRB/pl/19206992/The-Laboratory?layout=1"
)


def add_url(dj_name, dj_url):
    if dj_name in urls.keys():
        print(f"url already exists for {dj_name}")
        return
    urls[dj_name] = dj_url


def find_playlists(dj_name="thoge", max_pages=100):
    if not (dj_name in urls.keys()):
        print(f"no url yet for {dj_name}")
        return
    dj_url = urls[dj_name]
    base_url = dj_url[: len(dj_url) - 1]
    playlist_list = []
    seen_links = set()
    page = 1

    while page <= max_pages:
        response = requests.get(f"{base_url}{page}")
        soup = BeautifulSoup(response.text, "html.parser")
        link_rows = soup.select(".link.row")

        if not link_rows:
            break

        for link in link_rows:
            href = link.get("href")
            if href not in seen_links:
                seen_links.add(href)
                playlist_list.append(href)

        page += 1

    return playlist_list


def find_songs(spinitron_url=test_playlist_url):
    song_list = []

    # Fetch the HTML content of the Spinitron page
    if spinitron_url[:26] != "https://playlists.wprb.com":
        spinitron_url = "https://playlists.wprb.com" + spinitron_url
    response = requests.get(spinitron_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the specified line using the .spin-text class
    spin_text_elements = soup.select(".spin-text")

    # Extract the track, artist, and album from the spin_text_element
    for spin_text_element in spin_text_elements:
        if spin_text_element:
            artist = (
                spin_text_element.select_one(".artist").get_text(strip=True)
                if spin_text_element.select_one(".artist")
                else ""
            )
            song = (
                spin_text_element.select_one(".song").get_text(strip=True)
                if spin_text_element.select_one(".song")
                else ""
            )
            release = (
                spin_text_element.select_one(".release").get_text(strip=True)
                if spin_text_element.select_one(".release")
                else ""
            )
            current_track = (song, artist, release)

            song_list.append(current_track)

    return song_list


def all_dj_songs(dj_name="thoge"):
    if not (dj_name in urls.keys()):
        print(f"no url yet for {dj_name}")
        return
    playlists = find_playlists(dj_name)
    all_songs = []
    for playlist in playlists:
        all_songs.extend(find_songs(spinitron_url=playlist))
    return list(set(all_songs))


def songs_to_df(songs):
    return pd.DataFrame(songs, columns=["Artist", "Song", "Release"])


# assumes we already have url
def dj_name_to_csv(dj_name="thoge"):
    if not (dj_name in urls.keys()):
        print(f"no url yet for {dj_name}")
        return
    songs = all_dj_songs(dj_name)
    with open(
        f"dj_songs/{dj_name}_songs.csv", "w", newline="", encoding="utf-8"
    ) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Song", "Artist", "Release"])  # Write header
        writer.writerows(songs)


def top_artists_pie_chart(dj_name="thoge", threshold=5):
    if not (dj_name in urls.keys()):
        print(f"no songs yet for {dj_name}")
        return
    df = pd.read_csv(f"dj_songs/{dj_name}_songs.csv")
    artist_song_counts = df["Artist"].value_counts()

    # Step 3: Filter artists with more than one song and combine the rest into 'Other'
    filtered_artists = artist_song_counts[artist_song_counts > threshold]
    other_artists_count = artist_song_counts[artist_song_counts <= threshold].sum()

    # # Add the 'Other' category
    # filtered_artists['Other'] = other_artists_count

    # Step 4: Plot the pie chart
    plt.figure(figsize=(10, 8))
    filtered_artists.plot.pie(autopct="%1.1f%%", startangle=140)
    plt.title(f"Artists Played at least {threshold} times ({dj_name})")
    plt.ylabel("")  # Hide the y-label
    plt.show()


def top_songs(dj_name="thoge", threshold=2):
    if not (dj_name in urls.keys()):
        print(f"no songs yet for {dj_name}")
        return
    df = pd.read_csv(f"dj_songs/{dj_name}_songs.csv")
    artist_song_counts = df["Song"].value_counts()

    # Step 3: Filter artists with more than one song and combine the rest into 'Other'
    filtered_songs = artist_song_counts[artist_song_counts > threshold]
    other_songs_count = artist_song_counts[artist_song_counts <= threshold].sum()

    # Step 4: Plot the pie chart
    print(filtered_songs)


def top_n_artist_players(artist_name="Radiohead", n=10):
    for dj_name in url_keys:
        if not (dj_name in urls.keys()):
            print(f"no songs yet for {dj_name}")
            return
        df = pd.read_csv(f"dj_songs/{dj_name}_songs.csv")
        radiohead_count = df["Artist"].value_counts().get(artist_name, 0)
        dj_rhcounts[dj_name] = radiohead_count
    top_5_djs = Counter(dj_rhcounts).most_common(n)
    print(f"Top {n} DJs who have played {artist_name} the most:")
    for dj, count in top_5_djs:
        print(f"{dj}: {count} plays")


# main function
if __name__ == "__main__":
    top_n_artist_players("Squid", 10)
    # for dj_name in url_keys[4:]: # still need to do Pat's
    #     dj_name_to_csv(dj_name=dj_name)
    #     break
    # dj_name_to_csv(dj_name="DJ NEM")
    # top_artists_pie_chart(dj_name="Abe", threshold=5)
