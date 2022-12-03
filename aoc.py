def read_input(cookie_file, output_dir, year, day):
    import requests, os

    with open(cookie_file) as f:
        cookies = {"session": f.read()}
        r = requests.post(
            f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies
        )
        outpath = os.path.join(output_dir, f"{day}.txt")
        with open(outpath, "wb") as file:
            file.write(r.content)


if __name__ == "__main__":
    pass
