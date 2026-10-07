"""Критические значения d_L, d_U теста Дарбина–Уотсона.

    python tables/dw_critical_values.py          # пересчитать таблицы (.csv и .md рядом со скриптом)
    python tables/dw_critical_values.py --check  # только сверка с известными табличными точками

Границы — квантили уровня alpha двух отношений квадратичных форм (Durbin, Watson, 1951):

    d_L:  sum_{i=1}^{m} lambda_i     xi_i^2 / sum xi_i^2,
    d_U:  sum_{i=1}^{m} lambda_{i+k} xi_i^2 / sum xi_i^2,   m = n - k - 1,

где lambda_i = 2(1 - cos(pi i / n)), i = 1..n-1, xi_i — независимые N(0, 1),
n — число наблюдений, k — число регрессоров без константы (модель с константой).

P(отношение < d) = P(sum (lambda_i - d) xi_i^2 < 0) считается точно формулой Имхофа (1961),
квантиль находится решением уравнения. Моделирование не используется.
"""
import sys

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

ALPHAS = [0.05, 0.01]
K_VALUES = range(1, 11)
# 161, 163, 187, 199, 490 — размеры выборок в задачах курса (листок 11, разбор diagnostic-acorr)
N_VALUES = sorted(list(range(6, 41)) + list(range(45, 101, 5))
                  + [150, 200, 250, 300, 400, 500, 750, 1000]
                  + [161, 163, 187, 199, 490])


def prob_negative(a):
    """P(sum a_i xi_i^2 < 0) по формуле Имхофа."""
    def integrand(u):
        theta = 0.5 * np.sum(np.arctan(a * u))
        log_rho = 0.25 * np.sum(np.log1p((a * u) ** 2))
        return np.sin(theta) * np.exp(-log_rho) / u
    # при u -> 0 подынтегральная функция стремится к sum(a)/2; хвост убывает как u^(-m/2)
    value, _ = quad(integrand, 0, np.inf, limit=2000, epsabs=1e-10, epsrel=1e-10)
    return 0.5 - value / np.pi


def bounds(n, k, alpha):
    """(d_L, d_U) для n наблюдений, k регрессоров без константы, уровня alpha; None, если не определены."""
    m = n - k - 1
    if m < 1:
        return None
    lam = 2 * (1 - np.cos(np.pi * np.arange(1, n) / n))
    result = []
    for values in (lam[:m], lam[k:k + m]):
        if m == 1:
            # отношение вырождено в константу: квантиль не зависит от alpha
            result.append(float(values[0]))
            continue
        lo, hi = values.min() + 1e-9, values.max() - 1e-9
        result.append(brentq(lambda d: prob_negative(values - d) - alpha, lo, hi, xtol=1e-9))
    return tuple(result)


# Контрольные точки из опубликованных таблиц (Savin, White, 1977; записаны по памяти, поэтому
# допуск — единица третьего знака): (n, k, alpha) -> (d_L, d_U)
KNOWN = {
    (15, 1, 0.05): (1.077, 1.361),
    (30, 1, 0.05): (1.352, 1.489),
    (30, 3, 0.05): (1.214, 1.650),
    (100, 1, 0.05): (1.654, 1.694),
    (100, 5, 0.05): (1.571, 1.780),
    (200, 1, 0.05): (1.758, 1.779),
    (30, 1, 0.01): (1.134, 1.264),
    (100, 1, 0.01): (1.522, 1.562),
}


def check():
    worst = 0.0
    for (n, k, alpha), expected in KNOWN.items():
        got = bounds(n, k, alpha)
        diff = max(abs(g - e) for g, e in zip(got, expected))
        worst = max(worst, diff)
        print(f'n={n:3d} k={k} alpha={alpha}: {got[0]:.4f} {got[1]:.4f}  таблица {expected[0]:.3f} {expected[1]:.3f}')
        assert diff < 0.0011, f'расхождение с таблицей для n={n}, k={k}, alpha={alpha}'
    print(f'сверка пройдена, наибольшее расхождение {worst:.4f}')


def markdown(table):
    """Таблицы для чтения: по одной на уровень значимости и на группу k (1–5, 6–10)."""
    lines = ['# Критические значения теста Дарбина–Уотсона', '',
             'Нижняя $d_L$ и верхняя $d_U$ границы для модели с константой: $n$ — число наблюдений, '
             '$k$ — число регрессоров без константы. Значения вычислены точно (формула Имхофа), '
             'скрипт — `dw_critical_values.py`; те же числа в файле `dw-critical-values.csv`.', '',
             'Правило решения для статистики $DW$ на уровне значимости $\\alpha$ (односторонний тест):', '',
             '| Область | Вывод |', '|:--|:--|',
             '| $DW < d_L$ | положительная автокорреляция |',
             '| $d_L \\le DW \\le d_U$ | зона неопределённости |',
             '| $d_U < DW < 4 - d_U$ | автокорреляции нет |',
             '| $4 - d_U \\le DW \\le 4 - d_L$ | зона неопределённости |',
             '| $DW > 4 - d_L$ | отрицательная автокорреляция |', '']
    for alpha in ALPHAS:
        for ks in (range(1, 6), range(6, 11)):
            lines += [f'## Уровень значимости {alpha * 100:g}%, k = {ks[0]}–{ks[-1]}', '']
            lines.append('| n | ' + ' | '.join(f'k={k}: $d_L$ | $d_U$' for k in ks) + ' |')
            lines.append('|--:|' + '--:|' * (2 * len(ks)))
            for n in N_VALUES:
                cells = []
                for k in ks:
                    value = table.get((alpha, n, k))
                    cells += [f'{value[0]:.3f}', f'{value[1]:.3f}'] if value else ['—', '—']
                if any(cell != '—' for cell in cells):
                    lines.append(f'| {n} | ' + ' | '.join(cells) + ' |')
            lines.append('')
    return '\n'.join(lines)


if __name__ == '__main__':
    check()
    if '--check' in sys.argv:
        sys.exit()
    here = __file__.rsplit('/', 1)[0]
    table = {}
    for alpha in ALPHAS:
        for n in N_VALUES:
            for k in K_VALUES:
                # как в таблицах Савина–Уайта, значения даются при n - k - 1 >= 4
                if n - k - 1 >= 4:
                    table[(alpha, n, k)] = bounds(n, k, alpha)
        print(f'alpha={alpha}: готово')
    with open(f'{here}/dw-critical-values.csv', 'w', encoding='utf-8') as f:
        f.write('alpha,n,k,dL,dU\n')
        for (alpha, n, k), (d_l, d_u) in table.items():
            f.write(f'{alpha},{n},{k},{d_l:.4f},{d_u:.4f}\n')
    with open(f'{here}/dw-critical-values.md', 'w', encoding='utf-8') as f:
        f.write(markdown(table))
    print(f'записано значений: {len(table)}')
