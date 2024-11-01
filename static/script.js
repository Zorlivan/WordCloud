document.getElementById("wordcloud-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    const response = await fetch('/generate-wordcloud', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const blob = await response.blob();
        const imgURL = URL.createObjectURL(blob);

        // 打开新页面并展示词云图
        const newWindow = window.open();
        newWindow.document.write(`
            <html>
            <head>
                <title>词云图</title>
                <style>
                    body { display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f8f9fa; }
                    img { max-width: 90%; max-height: 90%; }
                </style>
            </head>
            <body>
                <img src="${imgURL}" alt="词云图">
            </body>
            </html>
        `);
    } else {
        alert("生成词云时出错，请重试！");
    }
});