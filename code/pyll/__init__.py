from code.pyll.merge_covid_mort_life_expectancy import MergeMortalityLifeExpectancy


if __name__ == '__main__':
    mf = MergeMortalityLifeExpectancy('Czechia')
    mf.calc_pyll_cz()
    mf.calc_pyll_cz(start_age=40, end_age=64)

    bg = MergeMortalityLifeExpectancy('Bulgaria')
    bg.calc_pyll_cz(sheet_name='combined_without_unk')
    bg.calc_pyll_cz(start_age=40, end_age=64, sheet_name='combined_without_unk')