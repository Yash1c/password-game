from game import (
    verificar_regras_anteriores,
    soma_digitos_igual_25,
    contem_numero_romano,
    tem_palindromo_3_chars,
    tem_sequencia_crescente,
    tem_anagrama_ano,
    soma_digitos_primos_igual_13,
    eh_senha_perfeita,
)


def run_tests():
    passed = 0
    failed = 0

    def check(name, cond):
        nonlocal passed, failed
        if cond:
            passed += 1
        else:
            failed += 1
            print(f"FAIL: {name}")

    # 1) soma_digitos_igual_25
    check("sum25_true", soma_digitos_igual_25("Abc!9x7Y4z5#0"))  # 9+7+4+5+0 = 25
    check("sum25_false", not soma_digitos_igual_25("Abc!9x7Y4z5#1"))  # 26

    # 2) verificar_regras_anteriores até regra 5
    check(
        "regras_ate_5_true",
        verificar_regras_anteriores("Abc!9x7Y4z5#0", ate_regra=5),
    )
    check(
        "regras_ate_5_false_sum",
        not verificar_regras_anteriores("Abc!9x7Y4z5#1", ate_regra=5),
    )

    # 3) Romanos
    check("romano_true", contem_numero_romano("abcVIxyz"))
    check("romano_false", not contem_numero_romano("abcNNxyz"))

    # 4) verificar_regras_anteriores até regra 6
    check(
        "regras_ate_6_true",
        verificar_regras_anteriores("Abc!9x7Y4z5#0VI", ate_regra=6),
    )

    # 5) palíndromo de 3+ letras
    check("palindromo_true", tem_palindromo_3_chars("xxanaYY"))
    check("palindromo_false", not tem_palindromo_3_chars("abc123def"))

    # 6) sequência crescente contígua
    check("seq_true", tem_sequencia_crescente("ab123cd"))
    check("seq_false_noncontig", not tem_sequencia_crescente("a1b2c3"))

    # 7) anagrama de 2024/2025 em bloco contíguo
    check("anagrama_true", tem_anagrama_ano("xx2204yy"))
    check("anagrama_false_scattered", not tem_anagrama_ano("2a0b2c4"))

    # 8) soma de dígitos primos = 13
    check("primos_13_true", soma_digitos_primos_igual_13("a2b3c5d3"))  # 2+3+5+3
    check("primos_13_false", not soma_digitos_primos_igual_13("a2b2c2"))

    # 9) senha perfeita
    check("senha_perfeita_true", eh_senha_perfeita("abcAEIOU@#@xyz"))
    check("senha_perfeita_false_vogais", not eh_senha_perfeita("abc@#@xyz"))
    check("senha_perfeita_false_especiais", not eh_senha_perfeita("abcAEIOU@##xyz"))

    print(f"PASSED: {passed}")
    print(f"FAILED: {failed}")


if __name__ == "__main__":
    run_tests()
