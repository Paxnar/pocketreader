import bytereaders


def decodeCharacter(character: int):
    if character <= 0x01F0:
        return \
            ['␀', ' ', 'ぁ', 'あ', 'ぃ', 'い', 'ぅ', 'う', 'ぇ', 'え', 'ぉ', 'お', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ',
             'ご', 'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'っ', 'つ', 'づ', 'て', 'で', 'と',
             'ど',
             'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま',
             'み',
             'む', 'め', 'も', 'ゃ', 'や', 'ゅ', 'ゆ', 'ょ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'ァ', 'ア', 'ィ', 'イ',
             'ゥ',
             'ウ', 'ェ', 'エ', 'ォ', 'オ', 'カ', 'ガ', 'キ', 'ギ', 'ク', 'グ', 'ケ', 'ゲ', 'コ', 'ゴ', 'サ', 'ザ', 'シ', 'ジ', 'ス', 'ズ',
             'セ',
             'ゼ', 'ソ', 'ゾ', 'タ', 'ダ', 'チ', 'ヂ', 'ッ', 'ツ', 'ヅ', 'テ', 'デ', 'ト', 'ド', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'バ',
             'パ',
             'ヒ', 'ビ', 'ピ', 'フ', 'ブ', 'プ', 'ヘ', 'ベ', 'ペ', 'ホ', 'ボ', 'ポ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ャ', 'ヤ', 'ュ', 'ユ',
             'ョ',
             'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン', '０', '１', '２', '３', '４', '５', '６', '７', '８', '９', 'Ａ', 'Ｂ',
             'Ｃ',
             'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ',
             'Ｙ',
             'Ｚ', 'ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'ｉ', 'ｊ', 'ｋ', 'ｌ', 'ｍ', 'ｎ', 'ｏ', 'ｐ', 'ｑ', 'ｒ', 'ｓ', 'ｔ',
             'ｕ',
             'ｖ', 'ｗ', 'ｘ', 'ｙ', 'ｚ', '', '！', '？', '、', '。', '…', '・', '／', '「', '」', '『', '』', '（', '）', '♂', '♀',
             '＋',
             'ー', '×', '÷', '＝', '～', '：', '；', '．', '，', '♠', '♣', '♥', '♦', '★', '◎', '○', '□', '△', '◇', '＠', '♪',
             '％',
             '☀', '☁', '☂', '☃', '🙂', '😄', '☹', '😠', '⬆', '⬇', 'Zz', '円', '👝', '🔑', '💿', '✉', '💊', '🍒', '🔮',
             '💥',
             '←', '↑', '↓', '→', '►',
             '＆', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
             'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'À', 'Á',
             'Â',
             'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×',
             'Ø',
             'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í',
             'î',
             'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ', 'Œ', 'œ', 'Ş', 'ş',
             'ª',
             'º', 'er', 're', 'r', 'P', '¡', '¿', '!', '?', ',', '.', '…', '･', '/', '‘', '’', '“', '”', '„', '«', '»',
             '(',
             ')', '♂', '♀', '+', '-', '*', '#', '=', '&', '~', ':', ';', '♠', '♣', '♥', '♦', '★', '◎', '○', '□', '△',
             '◇',
             '@', '♪', '%', '☀', '☁', '☂', '☃', '🙂', '😄', '☹', '😠', '⬆', '⬇', 'Zz', ' ', 'e', 'PK', 'MN', ' ', ' ',
             ' ', ' ', ' ', ' ', '°', '_', '＿', '․', '‥', '', '', ''][character]


def get_player_name(data, offset):
    name = ''
    for i in range(8):
        letter = bytereaders.read16(data, offset + i * 2)
        if letter == 65535:
            break
        name += decodeCharacter(letter)
    return name
