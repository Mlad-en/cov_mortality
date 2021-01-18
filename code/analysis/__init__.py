from get_excess_mortality import calc_bg_excess_mortality
from code.scraping.excess_mortality_utils import get_mortality_in_bulgaria

if __name__ == '__main__':
    scraped_file = get_mortality_in_bulgaria()
    total_mortality = calc_bg_excess_mortality(scraped_file)
    mortaliry_oct_dec = calc_bg_excess_mortality(scraped_file, 43, 53)
    print(total_mortality)
    print(mortaliry_oct_dec)