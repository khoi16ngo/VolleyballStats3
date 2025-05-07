from calendar import c
import sys
from models.user_inputs import UserInputs
from services.data.data_cleaner import clean_text_file
from services.stat_builders.player_stat_builder import build_player_stats
from services.stat_builders.raw_stat_builder import build_raw_player_stats
from services.stat_collectors.assist_stat_collector import collect_assist_stats
from services.stat_collectors.attack_stat_collector import collect_attack_stats
from services.stat_collectors.block_stat_collector import collect_block_stats
from services.stat_collectors.dig_stat_collector import collect_dig_stats
from services.stat_collectors.free_ball_stat_collector import collect_free_ball_stats
from services.stat_collectors.serve_receive_stat_collector import collect_serve_receive_stats
from services.stat_collectors.serve_stat_collector import collect_serve_stats
from utilities.util_file import get_file_name_from_file_path, remove_file_extension, get_file_headers
from services.data.data_writer import print_stats_csv
from services.data.data_reader import read_data_file
from services.user_input_fetchers.action_fetcher import *
from services.user_input_fetchers.quality_fetcher import *

class Program:
    def __init__(self, user_inputs: UserInputs):
        self.user_inputs = user_inputs
        self.clean_file_paths = []

    def run(self):
        '''
        Run the program to calculate the stats for each player in each set and total stats for all players.
        The calculated stats will be written to a new file in the "./results/" directory.
        '''
        try:
            print("Starting program...")

            self._initialize_actions()
            self._initialize_qualities()

            self._clean_file_paths()

            # Calculate the stats for each player in each set    
            self._calculate_set_stats()

            # Calculate the total stats for each player in all sets
            self._calculate_total_stats()
            
            print("Finished program!")
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

    def _initialize_actions(self):
        '''
        Initialize the actions for the user inputs.
        The actions are set to the user inputs actions.
        '''
        serve_action = find_serve_action(self.user_inputs.actions)
        if serve_action is None:
            raise ValueError("Serve action not found in user inputs.")
        self.user_inputs.set_serve_action(serve_action)

        serve_receive_action = find_serve_receive_pass_action(self.user_inputs.actions)
        if serve_receive_action is None:
            raise ValueError("Serve receive action not found in user inputs.")
        self.user_inputs.set_serve_receive_pass_action(serve_receive_action)

        free_ball_action = find_free_ball_action(self.user_inputs.actions)
        if free_ball_action is None:
            raise ValueError("Free ball action not found in user inputs.")
        self.user_inputs.set_free_ball_action(free_ball_action)

        dig_action = find_dig_action(self.user_inputs.actions)
        if dig_action is None:
            raise ValueError("Dig action not found in user inputs.")
        self.user_inputs.set_dig_action(dig_action)

        set_action = find_set_action(self.user_inputs.actions)
        if set_action is None:
            raise ValueError("Set action not found in user inputs.")
        self.user_inputs.set_assist_action(set_action)

        attack_action = find_attack_action(self.user_inputs.actions)
        if attack_action is None:
            raise ValueError("Attack action not found in user inputs.")
        self.user_inputs.set_attack_action(attack_action)

        block_action = find_block_action(self.user_inputs.actions)
        if block_action is None:
            raise ValueError("Block action not found in user inputs.")
        self.user_inputs.set_block_action(block_action)
    
    def _initialize_qualities(self):
        '''
        Initialize the qualities for the user inputs.
        The qualities are set to the user inputs qualities.
        '''
        perfect_quality = find_perfect_quality(self.user_inputs.action_qualities)
        if perfect_quality is None:
            raise ValueError("Perfect quality not found in user inputs.")
        self.user_inputs.set_perfect_quality(perfect_quality)

        good_quality = find_good_quality(self.user_inputs.action_qualities)
        if good_quality is None:
            raise ValueError("Good quality not found in user inputs.")
        self.user_inputs.set_good_quality(good_quality)

        medium_quality = find_ok_quality(self.user_inputs.action_qualities)
        if medium_quality is None:
            raise ValueError("Medium quality not found in user inputs.")
        self.user_inputs.set_ok_quality(medium_quality)

        poor_quality = find_poor_quality(self.user_inputs.action_qualities)
        if poor_quality is None:
            raise ValueError("Poor quality not found in user inputs.")
        self.user_inputs.set_poor_quality(poor_quality)

        error_quality = find_error_quality(self.user_inputs.action_qualities)
        if error_quality is None:
            raise ValueError("Error quality not found in user inputs.")
        self.user_inputs.set_error_quality(error_quality)

    def _clean_file_paths(self):
        '''
        Clean the raw data files passed in by the user.
        The cleaned files will be saved in the "./data/cleaned/" directory.
        The cleaned files will be named "<file_name>_cleaned.txt" and will be in the "./data/cleaned/" directory.
        '''
        print("Cleaning raw data files...")
        cleaned_file_paths = []
        for file_path in self.user_inputs.raw_data_file_paths:
            cleaned_file_path = clean_text_file(file_path)

            if cleaned_file_path != "":
                cleaned_file_paths.append(cleaned_file_path)
        
        if len(cleaned_file_paths) == 0:
            raise Exception("No cleaned files found. Please check the raw data files.")
        
        self.clean_file_paths = cleaned_file_paths
        print("Finished cleaning raw data files!")


    def _calculate_set_stats(self):
        '''
        Calculate the stats for each player in each set.
        The stats are calculated by reading the raw data files and then calculating the stats for each player.
        It will create a new file for each set with the stats for each player.
        The file will be named "<file_name>_stats.txt" and will be in the "./data/results/" directory.
        '''
        print("Calculating sets stats...")

        for clean_file_path in self.clean_file_paths:
            print(f"Calculating set stats for file {clean_file_path}...")
            raw_players_stats = read_data_file(clean_file_path)

            calculated_player_stats = build_raw_player_stats(self.user_inputs, raw_players_stats)   

            total_player_stats = self._get_players_total_stats_from_raw_data(calculated_player_stats)

            # Aggregate the stats for each player in the set into a single list
            # and write to a new file
            headers = get_file_headers()
            all_stats = [headers] + total_player_stats
            file_name = get_file_name_from_file_path(clean_file_path)
            new_cleaned_file_name = "./data/results/" + remove_file_extension(file_name) + "_stats.txt"
            print_stats_csv(new_cleaned_file_name, all_stats)
            print(f"Finished calculating set stats for file {clean_file_path}!")
        print("Finished calculating sets stats!")

    def _calculate_total_stats(self):
        print("Calculating total stats...")
        raw_player_stats = []
        for clean_file_path in self.clean_file_paths:
            raw_player_stats += read_data_file(clean_file_path)

        calculated_player_stats = build_raw_player_stats(self.user_inputs, raw_player_stats)

        total_player_stats = self._get_players_total_stats_from_raw_data(calculated_player_stats)

        # Aggregate the total stats for each player in all raw data files passed in
        # and write to a new file
        headers = get_file_headers()
        all_stats = [headers] + total_player_stats
        print_stats_csv('./data/results/total_stats.csv', all_stats)
        print("Finished calculating total stats!")

    def _get_players_total_stats_from_raw_data(self, calculated_players_stats: dict) -> list:
        total_player_stats = []
        for player in self.user_inputs.players:
            player_stat = build_player_stats(self.user_inputs, player, calculated_players_stats)
            
            total_player_stat = [player.name]
            total_player_stat += collect_attack_stats(player_stat)
            total_player_stat += collect_block_stats(player_stat)
            total_player_stat += collect_assist_stats(player_stat)
            total_player_stat += collect_free_ball_stats(player_stat)
            total_player_stat += collect_dig_stats(player_stat)
            total_player_stat += collect_serve_receive_stats(player_stat)
            total_player_stat += collect_serve_stats(player_stat)

            total_player_stats.append(total_player_stat)
        return total_player_stats