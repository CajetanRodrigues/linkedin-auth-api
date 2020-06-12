import LinkedInProfileScraper from 'linkedin-profile-scraper';
(async() => {
  const scraper = new LinkedInProfileScraper({
    sessionCookieValue: 'AQEDASXxNjID7M6PAAABcoXicbgAAAFyqe71uE0ATGrmQXIpwUkfH3p6VtLoNg2Dk3xcZuK3Sy_U0X8x42ScbogluiuFHB1kHDCCkUAhtkek2T1XDEZFblonlILIl933cyQp80RAzN_UPQg2o8XjSRp1',
    keepAlive: false
  });

  // Prepare the scraper
  // Loading it in memory
  await scraper.setup()

  const result = await scraper.run('https://www.linkedin.com/in/rodriguescajetan/')
  
  console.log(result)
})()