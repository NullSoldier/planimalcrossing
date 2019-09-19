# Stardew Valley farm planner
Source code of https://planimalcrossing.com

# Author
Kristin Murray @kem226

Forked from Stardew Valley Planner by Henrik Peinar @hpeinar 

# How to contribute
- Make PR
- I'll review it and merge if it checks out
- I'll update https://stardew.info/planner/ with your code in it so other people can also enjoy new features
- I'll add you to contributors list (feel free to do so in the PR).

# Feature suggestions not yet implemented
- QR code patterns
- Mobile design/support
- Full rendering so buildings etc can be fully drawn out


# Donate
Donations in any sum are very appreciated.     
[![](https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_37x23.jpg)](https://www.paypal.me/froshty)

# Installation & running
## Alternative 1
`npm install`    
`node index.js`     
`open http://127.0.0.1:3000`

# Contributors
- None yet :)

# Integration
POST `/api/import`     
CORS enabled endpoint which imports given save game file to the planner.     
Expects saveGame.xml or saveGame.zip as file parameter in the post. Please note that it implements regular zip format, not gzip.    
    
Note: This endpoint is rate limited to 600 requests per 15m (40 requests per minute)         
Note: saveGame.xml limit is 25mb    
      
Usage:      
`curl --form "file=@saveFile.xml" https://planimalcrossing.com/api/import`    
      
Response:     
```json
{
  "id": "readable-id-of-the-save",
  "absolutePath": "https://planimalcrossing.com/nl/readable-id-of-the-save"
}
```
     
Error response:     
```json 
{
  "message": "Missing file"
}
```

# Credits
- Based on Stardew Valley planner by Hendrik Peinar https://github.com/hpeinar/stardewplanner/

# License
Animal Crossing by © 2001 - 2017 Nintendo. Nintendo properties are trademarks of Nintendo.
Planimalcrossing licensed under the [Apache License v2](https://github.com/kem226/planimalcrossing/blob/master/LICENSE.md)
