const puppeteer = require('puppeteer');
const fs = require('fs') 
let txt = process.argv[2];
    (async () => {
        console.log(txt)
        console.log("running...");
        const browser = await puppeteer.launch();
        try {
            const ggl = await browser.newPage();
            await ggl.setExtraHTTPHeaders({
                'Accept-Language': 'en-GB'
            })

            await ggl.goto(("https://google.com/"), {waitUntil: 'networkidle2'});
            await ggl.keyboard.type(txt);
            await ggl.keyboard.press("Enter");
            let element = ""
            let text = ""
            try{
                await ggl.waitForSelector(".e24Kjd", { timeout: 2000});
                element = await ggl.$(".e24Kjd");
                text = await ggl.evaluate(element => element.textContent, element);
            }
            catch(err){
                try {
                    await ggl.waitForSelector(".Z0LcW", { timeout: 2000});
                    element = await ggl.$(".Z0LcW");
                    text = await ggl.evaluate(element => element.textContent, element);
                }
                catch(err) {
                    try {
                        await ggl.waitForSelector(".M1CzJc.PZPZlf.MtKf9c", { timeout: 2000});
                        element = await ggl.$(".M1CzJc.PZPZlf.MtKf9c");
                        text = await ggl.evaluate(element => element.textContent, element);
                    }
                    catch(err) {
                        try {
                            await ggl.waitForSelector(".dDoNo.vk_bk.gsrt", { timeout: 2000});
                            element = await ggl.$(".dDoNo.vk_bk.gsrt");
                            text = await ggl.evaluate(element => element.textContent, element); 
                        }
                        catch(err){
                            text = "Sorry, I can't answer to this"
                        }
                    }
                }
            }

            fs.writeFile('Output.txt', text, (err) => { 
                if (err) throw err; 
            }) 

            await browser.close();
        
        }
        catch (err){
            console.error("Perr: ", err.message);
            await browser.close();
        }  
            
        })();
