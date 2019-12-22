const fs = require("fs");
const puppeteer = require('puppeteer');
let txt = process.argv[2];

    (async () => {
        console.log("running...");
        const browser = await puppeteer.launch({headless: false});
        try {
            const yt = await browser.newPage();
        
            await yt.goto('https://youtube.com/', {waitUntil: 'networkidle2'});
            await yt.setDefaultNavigationTimeout(0); 
        
            let search = "#search"
        
            await yt.waitForSelector(search);
            await yt.click(search);
            await yt.keyboard.type(txt);
            await yt.click("#search-icon-legacy");
            await yt.waitForSelector(".ytd-video-renderer");
            await yt.click(".ytd-video-renderer:first-child");
            await yt.waitForSelector(".ended-mode", { timeout: 0});
            await browser.close();
            
            // const memes = await jeja.$$eval('.ob-image-j', link => { return link.map(src => src.src).slice(0,8) });
        
            // const upVotes = await jeja.$$eval('.cnt_votes_up', votes => { return votes.map(vote => parseInt(vote.innerHTML) )});
        
        
        }
        catch (err){
            console.error("Perr: ", err.message);
        }  
            
        })();
