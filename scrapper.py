import requests

def get_latest_jobs():
  url = "https://indeed-indeed.p.rapidapi.com/apisearch"
    
  querystring = {"publisher":"<REQUIRED>","v":"2","format":"json","callback":"<REQUIRED>","q":"java","l":"austin, tx","sort":"<REQUIRED>","radius":"25","st":"<REQUIRED>","jt":"<REQUIRED>","start":"<REQUIRED>","limit":"<REQUIRED>","fromage":"<REQUIRED>","highlight":"<REQUIRED>","filter":"<REQUIRED>","latlong":"<REQUIRED>","co":"<REQUIRED>","chnl":"<REQUIRED>","userip":"<REQUIRED>","useragent":"<REQUIRED>"}
   # You may need to provide authentication or API key
   headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "indeed-indeed.p.rapidapi.com"
}
 
    # Specify any parameters for your job search
    params = {
        'role': 'full stack developer',
        'location': 'anywhere',
        'experience': 'senior',
        'limit': 10  # Number of jobs to fetch
    }

    try:





response = requests.get(url, headers=headers, params=querystring)

print(response.json())

        for job in jobs:
            print(f"Job Title: {job['title']}")
            print(f"Company: {job['company']}")
            print(f"Location: {job['location']}")
            print(f"Link: {job['url']}")
            print("\n")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching job listings: {e}")

if __name__ == "__main__":
    get_latest_jobs()
