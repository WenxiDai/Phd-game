const express = require('express');

let port = 8000;
let app = express();
    app.use(express.static('./dist'));
    
    // Add a route for the new game interface
    app.get('/new', (req, res) => {
        res.sendFile('index-new.html', { root: './dist' });
    });
    
    app.listen(port, () => {
    console.log(`Server started on port ${port}.\n You can navigate to new interface at http://localhost:${port}/new`);
});