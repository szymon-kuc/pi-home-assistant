const puppeteer = require('puppeteer');
let txt = process.argv[2];
    (async () => {
        console.log("running...");
        const browser = await puppeteer.launch({headless: false});
        try {
            const yt = await browser.newPage();
        
            await yt.goto(('https://youtube.com/watch?v='+txt), {waitUntil: 'networkidle2'});
            await yt.setDefaultNavigationTimeout(0); 

            await yt.waitForSelector(".ytp-play-button");
            await yt.click(".ytp-play-button");
            
            await yt.waitForSelector(".ended-mode", { timeout: 0});
            await browser.close();
        
        }
        catch (err){
            console.error("Perr: ", err.message);
        }  
            
        })();
