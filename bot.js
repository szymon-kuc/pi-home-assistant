const puppeteer = require('puppeteer');
let txt = process.argv[2];
    (async () => {
        console.log("running...");
        const browser = await puppeteer.launch({headless: false});
        try {
            const yt = await browser.newPage();
        
            await yt.goto('https://youtube.com/', {waitUntil: 'networkidle2'});
            await yt.setDefaultNavigationTimeout(0); 
        
            let search = "#search";
        
            await yt.waitForSelector(search);
            await yt.click(search);
            await yt.keyboard.type(txt);
            await yt.click("#search-icon-legacy");
            await yt.waitForSelector(".ytd-video-renderer");
            await yt.click(".ytd-video-renderer:first-child");
            await yt.waitForSelector(".ended-mode", { timeout: 0});
            await browser.close();
        
        }
        catch (err){
            console.error("Perr: ", err.message);
        }  
            
        })();
