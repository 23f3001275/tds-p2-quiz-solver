from bs4 import BeautifulSoup
import base64

def parse_quiz(html: str):
    soup = BeautifulSoup(html, "html.parser")

    # Read visible text
    text = soup.get_text(" ", strip=True)

    # Detect base64-encoded content inside <script>
    scripts = soup.find_all("script")
    decoded = None
    for s in scripts:
        if "atob(" in s.text:
            # Extract the base64 argument
            import re
            encoded = re.search(r"atob\(`([^`]+)`\)", s.text)
            if encoded:
                decoded = base64.b64decode(encoded.group(1)).decode()

    # Simplified extraction
    question = decoded or text

    # Extract submit URL from decoded text or HTML
    submit_url = None
    if "submit" in question:
        import re
        m = re.search(r'https?://[^\s"]+', question)
        if m:
            submit_url = m.group(0)

    return question, submit_url, {"html": html, "decoded": decoded}
