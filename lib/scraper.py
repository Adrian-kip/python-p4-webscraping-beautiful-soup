from bs4 import BeautifulSoup
import requests

def scrape_flatiron_school():
    # Set up headers to mimic a browser visit
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Make the request to Flatiron School's website
        print("Fetching Flatiron School website...")
        response = requests.get("https://flatironschool.com/", headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the main heading
        main_heading = soup.select_one('.heading-financier')
        if main_heading:
            print("\nMain Heading:", main_heading.get_text(strip=True))
        
        # Extract navigation links
        print("\nMain Navigation Links:")
        nav_links = soup.select('nav a')
        for link in nav_links[:5]:  # Print first 5 to avoid too much output
            print(f"{link.get_text(strip=True):<20} -> {link['href']}")
        
        # Extract featured courses (if available)
        print("\nFeatured Courses:")
        courses = soup.select('.heading-60-black.color-black.mb-20')
        for course in courses:
            course_title = course.get_text(strip=True)
            if course_title and "Choose Your Course" not in course_title:
                print("-", course_title)
        
        # Extract footer information
        footer = soup.select_one('footer')
        if footer:
            print("\nFooter Copyright:", footer.select_one('p').get_text(strip=True))
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    scrape_flatiron_school()