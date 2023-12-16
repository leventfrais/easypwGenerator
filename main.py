from src.myConsts import create_parser
from src.nameProcess import process_name
from src.gen_birth import generatePW_birth
from src.birthProcess import process_birth

parser = create_parser()

args = parser.parse_args()

# 处理 name 与 idName (真名与网名 首字母题蛆 大小写化 并合并)
processedName = process_name(args.name, args.idName)
# print(processedName)

# 读取 additional 文件 并合并 add (如果有)
with open('txt/additionalWords.txt', 'r', encoding='utf-8') as file:
    additionalWords = [line.strip() for line in file.readlines()]
    # print(additionalWords)

if args.addition:
    for s in [args.addition]:
        additionalWords.extend(s)
    # print(additional_words)

if args.birth:
    processedBirth = process_birth(args.birth)
    generatePW_birth(processedName,processedBirth,additionalWords,args.length,args.conChar)

print(args)
