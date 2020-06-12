const scrapedin = require('scrapedin')
const options = {
    email: 'cajetanrodrigues88@gmail.com',
    password: '*m70GskgNmmTSUmVQ#BHe!A*3D0aWk5w^0QsPPviRejXCJHdZM'
  }
  scrapedin(options)
  .then((profileScraper) => profileScraper('https://www.linkedin.com/in/rodriguescajetan/'))
  .then((profile) => console.log(profile))