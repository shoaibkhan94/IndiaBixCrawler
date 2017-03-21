# IndiaBixCrawler
A web crawler that crawls all the questions with answers and options on the website www.indiabix.com and saves them to a json object.

**Usage Instructions**

To crawl all links on website : ```python3 main.py```
The links will be crawled and stored to a file `crawled.txt`.

To crawl the questions in the links : `scrapy runspider scraper.py -o questions.json`

Sample Output JSON : 

`[{
	"optionE": [],
	"page_tag": "032002",
	"optionA": ["int=2, int=3, int=4"],
	"question": "What will be the output of the program?\n",
	"optionB": ["int=2, int=2, int=2"],
	"main_tag": "c-programming",
	"sub_tag": "c-preprocessor",
	"optionC": ["int=3, int=3, int=3"],
	"optionD": ["int=4, int=4, int=4"],
	"answer": ["A"],
	"code": "#include<stdio.h>\n#define PRINT(int) printf(\"int=%d, \", int);\n\nint main()\n{\n    int x=2, y=3, z=4;   \n    PRINT(x);\n    PRINT(y);\n    PRINT(z);\n    return 0;\n}\n"
}, {
	"optionE": [],
	"page_tag": "032002",
	"optionA": ["a = 10, b = 12"],
	"question": "What will be the output of the program?\r\n",
	"optionB": ["a = 12, b = 10"],
	"main_tag": "c-programming",
	"sub_tag": "c-preprocessor",
	"optionC": ["Error: Declaration not allowed in macro"],
	"optionD": ["Error: Undefined symbol 't'"],
	"answer": ["B"],
	"code": "#include<stdio.h>\r\n#define SWAP(a, b) int t; t=a, a=b, b=t;\r\nint main()\r\n{\r\n    int a=10, b=12;\r\n    SWAP(a, b);\r\n    printf(\"a = %d, b = %d\\n\", a, b);\r\n    return 0;\r\n}\r\n"
}]`