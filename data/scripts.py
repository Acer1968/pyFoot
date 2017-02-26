db_tables_create_scripts = {
    'Game':
        '''CREATE TABLE Game (
        e_id INT PRIMARY KEY NOT NULL,
        e_name TEXT NOT NULL,
        e_value Text NOT NULL
        ); ''',
    'League':
        '''CREATE TABLE League (
        l_id INT PRIMARY KEY NOT NULL,
        l_name TEXT NOT NULL,
        l_nation TEXT NOT NULL,
        l_year_founded INT NOT NULL,
        l_tier INT NOT NULL
        );''',
    'Nation':
        '''CREATE TABLE Nation (
        n_id INT PRIMARY KEY NOT NULL,
        n_name TEXT NOT NULL,
        n_language TEXT NOT NULL,
        n_confederation TEXT NOT NULL
        );''',
    'Team':
        '''CREATE TABLE Team (
        t_id INT PRIMARY KEY NOT NULL,
        t_current_league_id INT NOT NULL,
        t_year_founded INT NOT NULL,
        t_current_funds INT NOT NULL,
        t_name TEXT NOT NULL,
        t_mascot TEXT NOT NULL,
        t_short_name TEXT NOT NULL,
        t_manager TEXT NOT NULL,
        t_owner TEXT NOT NULL,
        t_grounds_name TEXT NOT NULL,
        t_city_name TEXT NOT NULL,
        t_currrent_mentality INT NOT NULL,
        t_current_form INT NOT NULL
        );''',
    'Team_Attribute':
        '''CREATE TABLE Team_Atrubute (
        ta_id INT PRIMARY_KEY_NOT_NULL,
        ta_team_id INT NOT NULL,
        ta_competition_id INT NOT NULL,
        ta_aggressiveness INT NOT NULL,
        ta_focus_attack INT NOT NULL,
        ta_focus_defend INT NOT NULL,
        ta_ability_youth_development INT NOT NULL,
        ta_ability_training_grounds INT NOT NULL,
        ta_ability_physio INT NOT NULL,
        ta_ability_scout INT NOT NULL,
        ta_coach_attacking INT NOT NULL,
        ta_coach_defending INT NOT NULL,
        ta_coach_goal INT NOT NULL,
        ta_coach_midfield INT NOT NULL
        );''',
    'Match':
        '''CREATE TABLE Match (
        m_id INT PRIMARY KEY NOT NULL,
        m_date INT NOT NULL,
        m_time INT NOT NULL,
        m_played INT NOT NULL,
        m_competition_stage TEXT NOT NULL,
        m_team_home_id INT NOT NULL,
        m_team_away_id INT NOT NULL,
        m_score_home INT NOT NULL,
        m_score_away INT NOT NULL,
        m_fouls_home INT NOT NULL,
        m_fouls_away INT NOT NULL,
        m_yellow_home INT NOT NULL,
        m_yellow_away INT NOT NULL,
        m_red_home INT NOT NULL,
        m_red_away INT NOT NULL,
        m_shots_on_target_home INT NOT NULL,
        m_shots_on_tarket_away INT NOT NULL,
        m_shots_off_target_home INT NOT NULL,
        m_shots_off_target_away INT NOT NULL,
        m_possession_home INT NOT NULL,
        m_possession_away INT NOT NULL
        );''',
    'Match_Player':
        '''CREATE TABLE Match_Player (
        mp_id INT PRIMARY KEY NOT NULL,
        mp_player_id INT NOT NULL,
        mp_match_id INT NOT NULL,
        mp_position_played TEXT NOT NULL,
        mp_started INT NOT NULL,
        mp_time_on INT NOT NULL,
        mp_time_off INT NOT NULL,
        mp_goals INT NOT NULL,
        mp_assists INT NOT NULL,
        mp_yellow INT NOT NULL,
        mp_red INT NOT NULL,
        mp_fouls INT NOT NULL,
        mp_shots_on_target INT NOT NULL,
        mp_shots_off_target INT NOT NULL,
        mp_passes_complete INT NOT NULL,
        mp_passes_incompplete INT NOT NULL,
        mp_tackles INT NOT NULL,
        mp_interceptions INT NOT NULL,
        mp_goals_stopped INT NOT NULL,
        mp_health_start INT NOT NULL,
        mp_health_stop INT NOT NULL,
        mp_injury INT NOT NULL
        );''',
    'Comment':
        '''CREATE TABLE Comment (
        cmt_id INT PRIMARY KEY NOT NULL,
        cmt_match_id INT NOT NULL,
        cmt_sequence INT NOT NULL,
        cmt_time INT NOT NULL,
        cmt_text TEXT NOT NULL
        );''',
    'Season':
        '''CREATE TABLE Season (
        s_id INT PRIMARY KEY NOT NULL,
        s_year INT NOT NULL,
        s_competition_id
        );''',
    'Season_Table':
        '''CREATE TABLE Season_Table (
        st_id INT PRIMARY KEY NOT NULL,
        st_season_id INT NOT NULL,
        st_team_id INT NOT NULL,
        st_matches_played INT NOT NULL,
        st_matches_won INT NOT NULL,
        st_matches_lost INT NOT NULL,
        st_matches_drawn INT NOT NULL,
        st_goals_for INT NOT NULL,
        st_goals_against INT NOT NULL,
        st_points INT NOT NULL
        );''',
    'Competition':
        '''CREATE TABLE (
        c_id INT PRIMARY KEY NOT NULL,
        c_name TEXT NOT NULL,
        c_common_name TEXT NOT NULL
        );''',
    'Player':
        '''CREATE TABLE Player (
        p_id INT PRIMARY KEY NOT NULL,
        p_nation_id INT NOT NULL,
        p_first_name TEXT NOT NULL,
        p_last_name TEXT NOT NULL,
        p_height INT NOT NULL,
        p_wight INT NOT NULL,
        p_birth_year INT NOT NULL,
        p_birth_month INT NOT NULL,
        p_birth_day_of_month
        p_footed TEXT NOT NULL,
        p_current_form INT NOT NULL,
        p_current_health INT NOT NULL,
        p_current_mentality INT NOT NULL,
        p_current_training INT NOT NULL,
        p_current_rating INT NOT NULL,
        p_potential_rating INT NOT NULL,
        p_potential_growth INT NOT NULL
        );''',
    'Player_Season':
        '''CREATE TABLE Player_Season (
        pa_id INT PRIMARY KEY NOT NULL,
        pa_player_id INT NOT NULL,
        pa_season_id INT NOT NULL,
        pa_average_rating INT NOT NULL,
        pa_average_health INT NOT NULL,
        pa_potential_rating INT NOT NULL,
        pa_goals INT NOT NULL,
        pa_assists INT NOT NULL,
        pa_yellow INT NOT NULL,
        pa_red INT NOT NULL,
        pa_fouls INT NOT NULL,
        pa_shots_on_target INT NOT NULL,
        pa_shots_off_target INT NOT NULL,
        pa_passes_copalete INT NOT NULL,
        pa_passes_incopaplete INT NOT NULL,
        pa_tackles INT NOT NULL,
        pa_interceptions INT NOT NULL,
        pa_goals_stopped INT NOT NULL,
        pa_times_injured INT NOT NULL
        );''',
    'Game_Sequence':
        '''CREATE TABLE Game_Sequence (
        sq_id INT PRIMARY KEY NOT NULL,
        sq_table TEXT NOT NULL,
        sq_next_id INT NOT NULL
        );'''
}


db_tables_populate_scripts = {
    'Game':
        '''
        INSERT INTO Game
        VALUES
        (1, 'player_name', ''),
        (2, 'player_team_id', ''),
        (3, 'season_id', ''),
        (4, 'seasons_played', '0'),
        (5, 'seasons_to_keep_comments', 'All'),
        (6, 'starting_funds', '10,000,000'),
        (7, 'host', 'None'),
        (8, 'port', '8666'),
        (9, 'current_date', '[dt]')
        ;'''.replace('[dt]',datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d')),
    'Game_Sequence':
        '''
        INSERT INTO Game_Sequence
        VALUES
        (1, 'League', 1),
        (2, 'Nation', 1),
        (3, 'Team', 1),
        (4, 'Team_Attributes', 1),
        (5, 'Match', 1),
        (6, 'Match_Player', 1),
        (7, 'Comment', 1),
        (8, 'Season', 1),
        (9, 'Season_Table', 1),
        (10, 'Competition', 1),
        (11, 'Player', 1),
        (12, 'Player_Season', 1)
        ;'''
}