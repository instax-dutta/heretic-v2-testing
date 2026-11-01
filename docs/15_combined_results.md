# Combined results from the first two runs

These numbers came from the earliest logs. They are kept for the record; the final comparison is in the README and `25_heretic_v2_indepth_testing_report.md`.

## Run 1

Best 0-refusal trial: trial 12, KL 1.6492. Parameters: start_layer_index 1, end_layer_index 14, preserve_good_behavior_weight 0.7533, steer_bad_behavior_weight 0.00025, overcorrect_relative_weight 1.2245, neighbor_count 11.

## Run 2

Best 0-refusal trial: trial 2, KL 3.3504. Parameters: start_layer_index 0, end_layer_index 14, preserve_good_behavior_weight 0.8014, steer_bad_behavior_weight 0.0391, overcorrect_relative_weight 0.2243, neighbor_count 14.

## Status

The target was 0/100 refusals with KL below 0.005. The best 0-refusal KL in these runs was 1.649, far above that. Many trials reached KL between 0 and 0.01 but had 90 or more refusals.

## What it means

Getting both low KL and zero refusals on this model was not possible with the settings tried. A lower KL means accepting some refusals, or changing the search.
