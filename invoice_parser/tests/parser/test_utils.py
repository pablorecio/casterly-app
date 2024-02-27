import pytest
from src.parser.utils import combine_lines, extract_lines_from_pdf


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        ([], []),
        (
            [
                "1PLATANO",
                "0,838 kg 1,99 €/kg 1,67",
                "1KIWI VERDE",
                "0,644 kg 2,95 €/kg 1,90",
            ],
            [
                "1PLATANO 0,838 kg 1,99 €/kg 1,67",
                "1KIWI VERDE 0,644 kg 2,95 €/kg 1,90",
            ],
        ),
        (
            [
                "1PATATAS GAJO 1,90",
                "1KIWI VERDE",
                "0,644 kg 2,95 €/kg 1,90",
            ],
            [
                "1PATATAS GAJO 1,90",
                "1KIWI VERDE 0,644 kg 2,95 €/kg 1,90",
            ],
        ),
    ],
)
def test_combine_lines(lines, expected):
    result = combine_lines(lines)

    assert result == expected


@pytest.mark.parametrize(
    ("path", "lines"),
    [
        (
            "invoice_parser/tests/parser/data/mercadona_01.pdf",
            [
                "MERCADONA, S.A.   A-46103834",
                "C/ PRAGA S/N",
                "11405 JEREZ DE LA FRONTERA",
                "TELÉFONO: 956806148",
                "19/02/2024 19:19  OP: 96938",
                "FACTURA SIMPLIFICADA: 3893-020-160319",
                "Descripción P. Unit Importe",
                "1PATATAS GAJO 1,90",
                "1+PROT NATILLA VAINI 1,75",
                "1GOLOSINAS MIX PICA 1,65",
                "1BOLSA PAPEL 0,10",
                "TOTAL (€) 5,40",
                "TARJETA BANCARIA 5,40",
                "IVA BASE IMPONIBLE (€) CUOTA (€)",
                "10% 4,82 0,48",
                "21% 0,08 0,02",
                "TOTAL 4,90 0,50",
                "TARJ. BANCARIA:  **** **** **** 3058",
                "N.C: 047321823  AUT: 834847",
                "AID: A0000000041010   ARC: 3030",
                "MASTERCARD",
                "Importe: 5,40 €    DEBIT MASTERCARD",
                "SE ADMITEN DEVOLUCIONES CON TICKET",
            ],
        ),
        (
            "invoice_parser/tests/parser/data/mercadona_02.pdf",
            [
                "MERCADONA, S.A.   A-46103834",
                "C/ PRAGA S/N",
                "11405 JEREZ DE LA FRONTERA",
                "TELÉFONO: 956806148",
                "05/02/2024 18:28  OP: 111712",
                "FACTURA SIMPLIFICADA: 3893-014-373943",
                "Descripción P. Unit Importe",
                "1LAVAV. MAQ. LIQUIDO 2,95",
                "1+PROT NATILLA VAINI 1,75",
                "1PATATAS GAJO 1,90",
                "1TORTITA MAIZ C/CHOCO 1,65",
                "1TORTITAS DE MAIZ 1,10",
                "1BOLSA RAFIA 0,65",
                "1LECHE SEMI S/LACT 5,70",
                "2COPOS DE AVENA 0,95 1,90",
                "1REBUENAS 1,20",
                "1BASTONCILLO FAMIL 0,90",
                "1SAL YODADA 0,35",
                "1F+L CARIBE S AZÚCAR 1,20",
                "1ARROZ COCIDO 1,15",
                "1LOMO ADOBADO 3,56",
                "1FRESÓN 3,26",
                "1XUXES TOP TEN 1,25",
                "1SALMOREJO FRESCO 1,30",
                "1FRITADA PISTO 1,30",
                "16 HUEVOS CAMPEROS 1,59",
                "1PLATANO",
                "0,838 kg 1,99 €/kg 1,67",
                "1KIWI VERDE",
                "0,644 kg 2,95 €/kg 1,90",
                "TOTAL (€) 38,23",
                "TARJETA BANCARIA 38,23",
                "IVA BASE IMPONIBLE (€) CUOTA (€)",
                "10% 16,74 1,67",
                "21% 4,71 0,99",
                "0% 14,12 0,00",
                "TOTAL 35,57 2,66",
                "TARJ. BANCARIA:  **** **** **** 3058",
                "N.C: 047321823  AUT: 898697",
                "AID: A0000000041010   ARC: 3030",
                "MASTERCARD",
                "Importe: 38,23 €   DEBIT MASTERCARD",
                "SE ADMITEN DEVOLUCIONES CON TICKET",
            ],
        ),
    ],
)
def test_extract_lines_from_pdf(path, lines):
    result = extract_lines_from_pdf(path)

    assert result == lines
