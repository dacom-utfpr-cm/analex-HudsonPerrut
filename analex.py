from automata.fa.Moore import Moore
import sys, os
from transicaoOriginal import transitions
from myerror import MyError

error_handler = MyError('LexerErrors')

global check_cm
global check_key


moore = Moore([ # ESTADOS
    'q0', 'q1_i', 'q2_in', 'q3_int', 'q4_intEspaco', 'q5_if', 'q6_ifEspaco', 'q7_e', 'q8_el', 'q9_els', 'q10_else',
    'q11_elseEspaco', 'q12_f', 'q13_fl', 'q14_flo', 'q15_floa', 'q16_float', 'q17_floatEspaco','q18_r', 'q19_re', 
    'q20_ret', 'q21_retu', 'q22_retur', 'q23_return', 'q24_returnEspaco', 'q25_v', 'q26_vo', 'q27_voi', 'q28_void',
    'q29_voidEspaco', 'q30_w', 'q31_wh', 'q32_whi', 'q33_whil', 'q34_while', 'q35_whileEspaco', 'q36_adicao', 
    'q37_subtracao', 'q38_multiplicacao', 'q39_divisao', 'q40_divisaoFinalizado', 'q41_maior', 'q42_maiorIgual', 
    'q43_menor', 'q44_menorIgual', 'q45_maiorFinalizado', 'q46_menorFinalizado', 'q47_atribuicao', 'q48_igual',
    'q49_atribuicao_finalizado', 'q50_exclamacao', 'q51_exclamacaoIgual', 'q52_virgula', 'q53_pontoVirgula', 'q54_ponto',
    'q55_leftParenteses', 'q56_rightParenteses', 'q57_leftColchetes', 'q58_rightColchetes', 'q59_leftChaves',
    'q60_rightChaves','q61_id', 'q62_idLeftParenteses', 'q63_idRightParenteses', 'q64_idLeftColchetes', 'q65_idRightColchetes', 'q66_idLeftChaves',
    'q67_idRightChaves', 'q68_idPontoVirgula', 'q69_idVirgula', 'q70_idEspaco','q71_idAdicao', 'q72_idSubtracao', 'q73_idMultiplicacao', 'q74_idDivisao',
    'q75_idMaior', 'q76_idMenor', 'q77_idAtribuicao', 'q78_idExclamacao', 'q79_number', 'q80_numberLeftParenteses', 'q81_numberRightParenteses', 'q82_numberLeftColchetes',
    'q83_numberRightColchetes', 'q84_numberLeftChaves', 'q85_numberRightChaves', 'q86_numberPontoVirgula', 'q87_numberVirgula', 'q88_numberEspaco',
    'q89_numberAdicao', 'q90_numberSubtracao', 'q91_numberMultiplicacao', 'q92_numberDivisao', 'q93_numberMaior', 'q94_numberMenor', 'q95_numberAtribuicao', 'q96_numberExclamacao',
    'q97_intLeftParenteses', 'q98_intRightParenteses','q99_ifLeftParenteses', 'q100_elseLeftChaves', 'q101_returnLeftParenteses', 'q102_returnPontoVirgula', 
    'q103_voidRightParenteses', 'q104_voidPontoVirgula', 'q105_whileLeftParenteses', 'q106_floatLeftParenteses', 'q107_floatRightParenteses',
    'q108_divisaoEqual', 'q109_divisaoId', 'q110_divisaoNumber', 'q111_divisaoMultiplicacao', 'q112_comentario', 'q113_comentarioMultiplicacao', 'q114_comentarioFinalizado', 'q115_idIgual'
],

[ # ALFABETO DE ENTRADA
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '+', '-', '*', '/', '<', '>', '=', '!', '(', ')', '[', ']', '{', '}', ';', ',', '.',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '\n'
],

[ # ALFABETO DE SAIDA
    'ID',
    'NUMBER'
    'INT',
    'IF',
    'ELSE',
    'RETURN',
    'VOID',
    'WHILE',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'GREATER',
    'GREATER_EQUAL',
    'LESS',
    'LESS_EQUAL',
    'ATTRIBUTION',
    'EQUALS',
    'DIFFERENT',
    'COMMA',
    'SEMICOLON',
    'LPAREN',
    'RPAREN'
    'LBRACKETS',
    'RBRACKETS',
    'LBRACES',
    'RBRACES',
],

transitions,

'q0', # ESTADO INICIAL

{ # TABELA DE SAÍDA
    'q0' : '',
    'q1_i' : '',
    'q2_in' : '',
    'q3_int' : '',
    'q4_intEspaco' : 'INT\n',
    'q5_if' : '',
    'q6_ifEspaco' : 'IF\n',
    'q7_e' : '',
    'q8_el' : '',
    'q9_els' : '',
    'q10_else' : '',
    'q11_elseEspaco' : 'ELSE\n',
    'q12_f' : '',
    'q13_fl' : '',
    'q14_flo' : '',
    'q15_floa' : '',
    'q16_float' : '',
    'q18_r' : '',
    'q17_floatEspaco' : 'FLOAT\n',
    'q19_re' : '',
    'q20_ret' : '',
    'q21_retu' : '',
    'q22_retur' : '',
    'q23_return' : '',
    'q24_returnEspaco' : 'RETURN\n',
    'q25_v' : '',
    'q26_vo' : '',
    'q27_voi' : '',
    'q28_void' : '',
    'q29_voidEspaco' : 'VOID\n',
    'q30_w' : '',
    'q31_wh' : '',
    'q32_whi' : '',
    'q33_whil' : '',
    'q34_while' : '',
    'q35_whileEspaco' : 'WHILE\n',
    'q36_adicao' : 'PLUS\n',
    'q37_subtracao' : 'MINUS\n',
    'q38_multiplicacao' : 'TIMES\n',
    'q39_divisao' : '',
    'q40_divisaoFinalizado' : 'DIVIDE\n',
    'q41_maior' : '',
    'q42_maiorIgual' : 'GREATER_EQUAL\n',
    'q45_maiorFinalizado' : 'GREATER\n',
    'q43_menor' : '',
    'q44_menorIgual' : 'LESS_EQUAL\n',
    'q46_menorFinalizado' : 'LESS\n',
    'q47_atribuicao' : '',
    'q48_igual' : 'EQUALS\n',
    'q49_atribuicao_finalizado' : 'ATTRIBUTION\n',
    'q50_exclamacao' : '',
    'q51_exclamacaoIgual' : 'DIFFERENT\n',
    'q52_virgula' : 'COMMA\n',
    'q53_pontoVirgula' : 'SEMICOLON\n',
    'q54_ponto' : '',
    'q55_leftParenteses' : 'LPAREN\n',
    'q56_rightParenteses' : 'RPAREN\n',
    'q57_leftColchetes' : 'LBRACKETS\n',
    'q58_rightColchetes' : 'RBRACKETS\n',
    'q59_leftChaves' : 'LBRACES\n',
    'q60_rightChaves' : 'RBRACES\n',
    'q61_id' : '',
    'q62_idLeftParenteses' : 'ID\nLPAREN\n',
    'q63_idRightParenteses' : 'ID\nRPAREN\n',
    'q64_idLeftColchetes' : 'ID\nLBRACKETS\n',
    'q65_idRightColchetes' : 'ID\nRB RACKETS\n',
    'q66_idLeftChaves' : 'ID\nLBRACES\n',
    'q67_idRightChaves' : 'ID\nRBRACES\n',
    'q68_idPontoVirgula' : 'ID\nSEMICOLON\n',
    'q69_idVirgula' : 'ID\nCOMMA\n',
    'q70_idEspaco' : 'ID\n',
    'q71_idAdicao' : 'ID\nPLUS\n',
    'q72_idSubtracao' : 'ID\nMINUS\n',
    'q73_idMultiplicacao' : 'ID\nTIMES\n',
    'q74_idDivisao' : 'ID\nDIVIDE\n',
    'q75_idMaior' : 'ID\nGREATER\n', #
    'q76_idMenor' : 'ID\nLESS\n', #
    'q77_idAtribuicao' : 'ID\nATTRIBUTION\n', #
    'q78_idExclamacao' : 'ID\nDIFFERENT\n', #
    'q79_number' : '',
    'q80_numberLeftParenteses' : 'NUMBER\nLPAREN\n',
    'q81_numberRightParenteses' : 'NUMBER\nRPAREN\n',
    'q82_numberLeftColchetes' : 'NUMBER\nLBRACKETS\n',
    'q83_numberRightColchetes' : 'NUMBER\nRBRACKETS\n',
    'q84_numberLeftChaves' : 'NUMBER\nLBRACES\n',
    'q85_numberRightChaves' : 'NUMBER\nRBRACES\n',
    'q86_numberPontoVirgula' : 'NUMBER\nSEMICOLON\n',
    'q87_numberVirgula' : 'NUMBER\nCOMMA\n',
    'q88_numberEspaco' : 'NUMBER\n',
    'q89_numberAdicao' : 'NUMBER\nPLUS\n',
    'q90_numberSubtracao' : 'NUMBER\nMINUS\n',
    'q91_numberMultiplicacao' : 'NUMBER\nTIMES\n',
    'q92_numberDivisao' : 'NUMBER\nDIVIDE\n',
    'q93_numberMaior' : 'NUMBER\nGREATER\n', #
    'q94_numberMenor' : 'NUMBER\nLESS\n', #
    'q95_numberAtribuicao' : 'NUMBER\nATTRIBUTION', #
    'q96_numberExclamacao' : 'NUMBER\nDIFFERENT\n', #
    'q97_intLeftParenteses' : 'INT\nLPAREN\n',
    'q98_intRightParenteses' : 'INT\nRPAREN\n',
    'q99_ifLeftParenteses' : 'IF\nLPAREN\n', 
    'q100_elseLeftChaves' : 'ELSE\nLBRACES\n', 
    'q101_returnLeftParenteses' : 'RETURN\nLPAREN\n',
    'q102_returnPontoVirgula' : 'RETURN\nSEMICOLON\n',
    'q103_voidRightParenteses' : 'VOID\nRPAREN\n',
    'q104_voidPontoVirgula' : 'VOID\nSEMICOLON\n',
    'q105_whileLeftParenteses' : 'WHILE\nLPAREN\n',
    'q106_floatLeftParenteses' : 'FLOAT\nLPAREN\n',
    'q107_floatRightParenteses' : 'FLOAT\nRPAREN\n',
    'q111_divisaoMultiplicacao' : '',
    'q112_comentario' : '',
    'q113_comentarioMultiplicacao' : '',
    'q114_comentarioFinalizado' : '',
})

def main():
    check_cm = False
    check_key = False
    
    for idx, arg in enumerate(sys.argv):
        #print("Argument #{} is {}".format(idx, arg))
        aux = arg.split('.')
        if aux[-1] == 'cm':
            check_cm = True
            idx_cm = idx

        if(arg == "-k"):
            check_key = True
    
    #print ("No. of arguments passed is ", len(sys.argv))

    if(len(sys.argv) < 3):
        raise TypeError(error_handler.newError(check_key, 'ERR-LEX-USE'))

    if not check_cm:
      raise IOError(error_handler.newError(check_key, 'ERR-LEX-NOT-CM'))
    elif not os.path.exists(sys.argv[idx_cm]):
        raise IOError(error_handler.newError(check_key, 'ERR-LEX-FILE-NOT-EXISTS'))
    else:
        data = open(sys.argv[idx_cm])
        source_file = data.read()

        if not check_cm:
            print("Def")
            print(moore)
            print("Entrada:")
            print(source_file)
            print("Lista de Tokens:")
        
        print(moore.get_output_from_string(source_file))


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(e)
    except (ValueError, TypeError):
        print(ValueError)