import nodriver
from nodriver_cf_bypass import CFBypass

async def main() -> None:
    browser: nodriver.Browser = await nodriver.start()
    browser_tab: nodriver.Tab = await browser.get("https://www.nowsecure.nl/")

    CFB: CFBypass = CFBypass(_browser_tab = browser_tab, _debug = True)
    result = await CFB.bypass(_max_retries = 10, _interval_between_retries = 1, _reload_page_after_n_retries = 0)

    if result:
        print("Cloudflare has been bypassed.")
        return None

    print("Couldn't bypass cloudflare for some reason.")

nodriver.loop().run_until_complete(main())
