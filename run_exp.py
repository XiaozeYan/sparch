#
# SPDX-FileCopyrightText: Copyright © 2022 Idiap Research Institute <contact@idiap.ch>
#
# SPDX-FileContributor: Alexandre Bittar <abittar@idiap.ch>
#
# SPDX-License-Identifier: BSD-3-Clause
#
# This file is part of the sparch package
#
"""
This is the script used to run experiments.
"""
import argparse
import logging

from sparch.exp import Experiment
from sparch.parsers.model_config import add_model_options
from sparch.parsers.training_config import add_training_options

logger = logging.getLogger(__name__)


def parse_args():

    parser = argparse.ArgumentParser(
        description="Model training on spiking speech commands datasets."
    )
    parser = add_model_options(parser)
    parser = add_training_options(parser)
    args = parser.parse_args()

    return args


def main(**arg_reference):
    """
    Runs model training/testing using the configuration specified
    by the parser arguments. Run `python run_exp.py -h` for details.
    """

    # Get experiment configuration from parser
    args = parse_args()

    # replace some key in args with parameters of main function so I can directly train with calling the main function
    args_dict:dict = vars(args)
    args_dict.update(arg_reference)
    args = argparse.Namespace(**args_dict)

    # Instantiate class for the desired experiment
    experiment = Experiment(args)

    # Run experiment
    experiment.forward()


if __name__ == "__main__":

    import torch
    seed = 0
    torch.manual_seed(seed)

    import numpy as np
    np.random.seed(seed)

    main(
        nb_hiddens = 128,
        model_type = "adLIF",
        dataset_name = "sc",
        data_folder = "./dataset/SpeechCommands/speech_commands_v0.02",
        # when use pretrained
        # use_pretrained_model = True,
        # load_exp_folder = "test/adLIF_sc",
        batch_size = 128,
        log_tofile = True
    )
