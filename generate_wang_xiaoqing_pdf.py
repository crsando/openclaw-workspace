from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm

OUT = '/home/ralmia/.openclaw/workspace/王小青-人物资料卡详细版.pdf'

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CNTitle', fontName='STSong-Light', fontSize=20, leading=24, alignment=TA_CENTER, textColor=colors.HexColor('#0f172a'), spaceAfter=8))
styles.add(ParagraphStyle(name='CNSubTitle', fontName='STSong-Light', fontSize=10.5, leading=14, alignment=TA_CENTER, textColor=colors.HexColor('#475569'), spaceAfter=10))
styles.add(ParagraphStyle(name='CNHeading', fontName='STSong-Light', fontSize=13, leading=18, textColor=colors.HexColor('#0f766e'), spaceBefore=8, spaceAfter=6))
styles.add(ParagraphStyle(name='CNBody', fontName='STSong-Light', fontSize=10.5, leading=16, textColor=colors.HexColor('#111827')))
styles.add(ParagraphStyle(name='CNNote', fontName='STSong-Light', fontSize=9.5, leading=14, textColor=colors.HexColor('#475569')))

story = []
story.append(Paragraph('王小青｜人物资料卡（详细版）', styles['CNTitle']))
story.append(Paragraph('截至 2026-04-15，基于公开资料整理', styles['CNSubTitle']))

summary_data = [
    [Paragraph('<b>核心身份</b>', styles['CNBody']), Paragraph('招商银行原副行长，曾任招商银行深圳分行行长、行长助理；曾任招商基金党委书记、总经理、董事长；曾任招商信诺人寿董事长、招商信诺资管董事长。', styles['CNBody'])],
    [Paragraph('<b>一句话概括</b>', styles['CNBody']), Paragraph('资管出身，横跨基金、保险、银行多个板块，兼具总部管理与一线经营经验的招商系金融高管。', styles['CNBody'])],
]

t = Table(summary_data, colWidths=[30*mm, 145*mm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
    ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#cbd5e1')),
    ('INNERGRID', (0,0), (-1,-1), 0.4, colors.HexColor('#e2e8f0')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
]))
story.append(t)
story.append(Spacer(1, 8))

story.append(Paragraph('一、基本信息', styles['CNHeading']))
basic_info = [
    '姓名：王小青',
    '性别：男',
    '出生年月：1971年10月',
    '籍贯：江苏南通',
    '学历：复旦大学政治经济学博士研究生',
    '其他公开学历：牛津大学 MBA',
    '职称：经济师',
]
story.append(ListFlowable([ListItem(Paragraph(x, styles['CNBody'])) for x in basic_info], bulletType='bullet'))

story.append(Paragraph('二、主要履历', styles['CNHeading']))
career = [
    '早年曾任职于中国农业银行、海通证券、中国证监会、天一证券。',
    '2007年8月—2020年3月：任职中国人保资产管理有限公司，历任总裁助理、副总裁、党委委员、党委副书记、投委会主任委员等。',
    '2020年3月：加入招商基金，任党委书记、董事、总经理。',
    '后续：在招商基金任董事长，并作为公司法定代表人相关事项办理对象。',
]
story.append(ListFlowable([ListItem(Paragraph(x, styles['CNBody'])) for x in career], bulletType='bullet'))

story.append(Paragraph('三、招商系任职脉络', styles['CNHeading']))
lineage = [
    '曾任招商信诺人寿保险有限公司董事长。',
    '曾任招商信诺资产管理有限公司董事长。',
    '曾任招商银行行长助理。',
    '曾任招商银行深圳分行行长。',
    '曾任招商银行副行长。',
]
story.append(ListFlowable([ListItem(Paragraph(x, styles['CNBody'])) for x in lineage], bulletType='bullet'))

story.append(Paragraph('四、关键节点', styles['CNHeading']))
key_nodes = [
    '2020年3月：加入招商基金。',
    '2021年6月：招商基金公告披露其任党委书记、董事、总经理，并办理法定代表人相关事项。',
    '2025年8月4日：招商银行公告披露，王小青因工作原因辞去副行长职务，自当日起生效。',
]
story.append(ListFlowable([ListItem(Paragraph(x, styles['CNBody'])) for x in key_nodes], bulletType='bullet'))

story.append(Paragraph('五、职业特征', styles['CNHeading']))
traits = [
    '资管背景深，从人保资管到招商基金路径清晰。',
    '综合金融经验完整，覆盖基金、保险、银行。',
    '兼具总行平台经验与深圳分行一线经营经验。',
]
story.append(ListFlowable([ListItem(Paragraph(x, styles['CNBody'])) for x in traits], bulletType='bullet'))

story.append(Paragraph('六、主要来源', styles['CNHeading']))
sources = [
    '1. 招商银行《关于副行长辞任的公告》：https://s3gw.cmbchina.com/lb5001-cmbweb-prd-1255000097/cmbir/20250804/1fb5a83a-8c79-429b-b382-847c7864e776.pdf',
    '2. 招商基金公告（2021-06-05）：https://www.cmfchina.com/web/fundnoticedetail/202313/index.html',
    '3. 招商基金文章（提及董事长王小青）：https://www.cmfchina.com/article/10166097/index.html',
    '4. 招商基金公告（2025-09-24）：https://www.cmfchina.com/web/noticedetails/220797/index.html',
    '5. 百度百科“王小青”：https://baike.baidu.com/item/王小青/56798697',
]
for s in sources:
    story.append(Paragraph(s, styles['CNNote']))
    story.append(Spacer(1, 2))

story.append(Spacer(1, 6))
story.append(Paragraph('说明：招商银行“原副行长”身份已由招商银行正式辞任公告确认；出生地、学历等基础信息主要来自公开百科资料，若用于正式尽调，建议继续以年报、任职公告、工商与监管披露信息逐条交叉验证。', styles['CNNote']))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm, topMargin=14*mm, bottomMargin=14*mm)
doc.build(story)
print(OUT)
