import math

MIXTURE_CMD = 0.8
INITIAL_HEADING_DEG = 270
INITIAL_ALTITUDE_FT = 10000
INITIAL_SPEED_FPS = 650
DEFAULT_EPISODE_TIME_S = 240.0
# TARGET_HDOT_RANGE = 40.0
# TARGET_PHI_RANGE = 0.01
MIN_STATE_QUALITY = 0.0  # terminate if state 'quality' is less than this
MAX_ALTITUDE_DEVIATION_FT = 10000  # terminate if altitude error exceeds this
MAX_HDOT_ERROR = 200 # ft/s
MAX_PHI_ERROR = 0.03 * math.pi


pot_delta_T_scale = 0.2

# Random hdot only
hdot_gamma = 0.995
hdot_kappa_long = 0.1e-6
hdot_kappa_lat = 1
hdot_potential_offset = -155 # Not necessary, just keeps rewards close to 0
hdot_w_hdot = 1
hdot_w_phi = 100


# Random hdot and turn rate
hdot_phi_gamma = 0.995
# hdot_phi_w_hdot = 0.5
# hdot_phi_w_phi = 4 # for phi
# hdot_phi_w_phi = 0.03
# hdot_phi_kappa_long = 0.1e-6
# hdot_phi_kappa_lat = 1

# TARGET_HDOT_RANGE = 20.0
# TARGET_PHI_RANGE = math.radians(1)
# hdot_phi_kappa_long = 0
# hdot_phi_kappa_lat = 0
# hdot_phi_potential_offset = 0
# hdot_phi_w_hdot = 1
# hdot_phi_w_phi = 0.2

TARGET_HDOT_RANGE = 20.0
TARGET_PHI_RANGE = math.radians(1)
hdot_phi_kappa_long = 0
hdot_phi_kappa_lat = 0
hdot_phi_potential_offset = 0
hdot_phi_w_hdot = 1
hdot_phi_w_phi = 0.1

# TARGET_HDOT_RANGE = 20.0
# TARGET_PHI_RANGE = math.radians(3)
# hdot_phi_kappa_long = 0
# hdot_phi_kappa_lat = 0
# hdot_phi_potential_offset = 0
# hdot_phi_w_hdot = 1
# hdot_phi_w_phi = 0.1

# TARGET_HDOT_RANGE = 20.0
# TARGET_PHI_RANGE = math.radians(5)
# hdot_phi_kappa_long = 0
# hdot_phi_kappa_lat = 100
# hdot_phi_potential_offset = -0.05
# hdot_phi_w_hdot = 1
# hdot_phi_w_phi = 0.06

# TARGET_HDOT_RANGE = 20.0
# TARGET_PHI_RANGE = math.radians(5)
# hdot_phi_kappa_long = 0
# hdot_phi_kappa_lat = 1
# hdot_phi_potential_offset = 0
# hdot_phi_w_hdot = 1
# hdot_phi_w_phi = 0.06

# hdot_phi_potential_offset = -0.1
# hdot_phi_kappa_long = 1
# hdot_phi_kappa_lat = 200