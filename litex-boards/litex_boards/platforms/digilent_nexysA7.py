#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2018-2019 Florent Kermarrec <florent@enjoy-digital.fr>
# Copyright (c) 2021 Michael T. Mayers <michael@tweakoz.com>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer
from litex.build.openocd import OpenOCD

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk / Rst
    ("clk100",    0, Pins("E3"),  IOStandard("LVCMOS33")),
    ("cpu_reset", 0, Pins("C12"), IOStandard("LVCMOS33")),

    # Leds
    ("user_led",  0, Pins("H17"), IOStandard("LVCMOS33")),
    ("user_led",  1, Pins("K15"), IOStandard("LVCMOS33")),
    ("user_led",  2, Pins("J13"), IOStandard("LVCMOS33")),
    ("user_led",  3, Pins("N14"), IOStandard("LVCMOS33")),
    ("user_led",  4, Pins("R18"), IOStandard("LVCMOS33")),
    ("user_led",  5, Pins("V17"), IOStandard("LVCMOS33")),
    ("user_led",  6, Pins("U17"), IOStandard("LVCMOS33")),
    ("user_led",  7, Pins("U16"), IOStandard("LVCMOS33")),
    ("user_led",  8, Pins("V16"), IOStandard("LVCMOS33")),
    ("user_led",  9, Pins("T15"), IOStandard("LVCMOS33")),
    ("user_led", 10, Pins("U14"), IOStandard("LVCMOS33")),
    ("user_led", 11, Pins("T16"), IOStandard("LVCMOS33")),
    ("user_led", 12, Pins("V15"), IOStandard("LVCMOS33")),
    ("user_led", 13, Pins("V14"), IOStandard("LVCMOS33")),
    ("user_led", 14, Pins("V12"), IOStandard("LVCMOS33")),
    ("user_led", 15, Pins("V11"), IOStandard("LVCMOS33")),

    # 7SEG DISPLAY
    ("segled_an",  0, Pins("J17"), IOStandard("LVCMOS33")),
    ("segled_an",  1, Pins("J18"), IOStandard("LVCMOS33")),
    ("segled_an",  2, Pins("T9 "), IOStandard("LVCMOS33")),
    ("segled_an",  3, Pins("J14"), IOStandard("LVCMOS33")),
    ("segled_an",  4, Pins("P14"), IOStandard("LVCMOS33")),
    ("segled_an",  5, Pins("T14"), IOStandard("LVCMOS33")),
    ("segled_an",  6, Pins("K2 "), IOStandard("LVCMOS33")),
    ("segled_an",  7, Pins("U13"), IOStandard("LVCMOS33")),

    ("segled_ca",  0, Pins("T10"), IOStandard("LVCMOS33")),
    ("segled_cb",  0, Pins("R10"), IOStandard("LVCMOS33")),
    ("segled_cc",  0, Pins("K16"), IOStandard("LVCMOS33")),
    ("segled_cd",  0, Pins("K13"), IOStandard("LVCMOS33")),
    ("segled_ce",  0, Pins("P15"), IOStandard("LVCMOS33")),
    ("segled_cf",  0, Pins("T11"), IOStandard("LVCMOS33")),
    ("segled_cg",  0, Pins("L18"), IOStandard("LVCMOS33")),
    ("segled_dp",  0, Pins("H15"), IOStandard("LVCMOS33")),

    ("rgb_led", 0,
        Subsignal("r", Pins("N15")),
        Subsignal("g", Pins("M16")),
        Subsignal("b", Pins("R12")),
        IOStandard("LVCMOS33"),
    ),
    ("rgb_led", 1,
        Subsignal("r", Pins("N16")),
        Subsignal("g", Pins("R11")),
        Subsignal("b", Pins("G14")),
        IOStandard("LVCMOS33"),
    ),

    # Switches
    ("user_sw",  0, Pins("J15"), IOStandard("LVCMOS33")),
    ("user_sw",  1, Pins("L16"), IOStandard("LVCMOS33")),
    ("user_sw",  2, Pins("M13"), IOStandard("LVCMOS33")),
    ("user_sw",  3, Pins("R15"), IOStandard("LVCMOS33")),
    ("user_sw",  4, Pins("R17"), IOStandard("LVCMOS33")),
    ("user_sw",  5, Pins("T18"), IOStandard("LVCMOS33")),
    ("user_sw",  6, Pins("U18"), IOStandard("LVCMOS33")),
    ("user_sw",  7, Pins("R13"), IOStandard("LVCMOS33")),
    ("user_sw",  8, Pins("T8 "),  IOStandard("LVCMOS33")),
    ("user_sw",  9, Pins("U8 "),  IOStandard("LVCMOS33")),
    ("user_sw", 10, Pins("R16"), IOStandard("LVCMOS33")),
    ("user_sw", 11, Pins("T13"), IOStandard("LVCMOS33")),
    ("user_sw", 12, Pins("H6 "),  IOStandard("LVCMOS33")),
    ("user_sw", 13, Pins("U12"), IOStandard("LVCMOS33")),
    ("user_sw", 14, Pins("U11"), IOStandard("LVCMOS33")),
    ("user_sw", 15, Pins("V10"), IOStandard("LVCMOS33")),

    # Buttons
    ("user_btn", 0, Pins("N17"), IOStandard("LVCMOS33")),
    ("user_btn", 1, Pins("M18"), IOStandard("LVCMOS33")),
    ("user_btn", 2, Pins("P17"), IOStandard("LVCMOS33")),
    ("user_btn", 3, Pins("M17"), IOStandard("LVCMOS33")),
    ("user_btn", 4, Pins("P18"), IOStandard("LVCMOS33")),

    # Serial
    ("serial", 0,
        Subsignal("tx", Pins("D4")),
        Subsignal("rx", Pins("C4")),
        IOStandard("LVCMOS33"),
    ),

    # SDCard
    ("spisdcard", 0,
        Subsignal("rst",  Pins("E2")),
        Subsignal("clk",  Pins("B1")),
        Subsignal("mosi", Pins("C1"), Misc("PULLUP True")),
        Subsignal("cs_n", Pins("D2"), Misc("PULLUP True")),
        Subsignal("miso", Pins("C2"), Misc("PULLUP True")),
        Misc("SLEW=FAST"),
        IOStandard("LVCMOS33"),
    ),
    ("sdcard", 0,
        Subsignal("rst",  Pins("E2"),          Misc("PULLUP True")),
        Subsignal("data", Pins("C2 E1 F1 D2"), Misc("PULLUP True")),
        Subsignal("cmd",  Pins("C1"),          Misc("PULLUP True")),
        Subsignal("clk",  Pins("B1")),
        Subsignal("cd",   Pins("A1")),
        Misc("SLEW=FAST"),
        IOStandard("LVCMOS33"),
    ),

    # SRAM
    ("cellularram", 0,
        Subsignal("addr", Pins(
            "J18 H17 H15 J17 H16 K15 K13 N15",
            "V16 U14 V14 V12 P14 U16 R15 N14",
            "N16 M13 V17 U17 T10 M16 U13"),
        ),
        Subsignal("data", Pins(
            "R12 T11 U12 R13 U18 R17 T18 R18",
            "F18 G18 G17 M18 M17 P18 N17 P17"),
        ),
        Subsignal("oen",  Pins("H14")),
        Subsignal("wen",  Pins("R11")),
        Subsignal("clk",  Pins("T15")),
        Subsignal("adv",  Pins("T13")),
        Subsignal("wait", Pins("T14")),
        Subsignal("cen",  Pins("L18")),
        Subsignal("ub",   Pins("J13")),
        Subsignal("lb",   Pins("J15")),
        Subsignal("cre",  Pins("J14")),
        Misc("SLEW=FAST"),
        IOStandard("LVCMOS33"),
    ),
    # DDR2 SDRAM
    ("ddram", 0,
        Subsignal("a", Pins(
            "M4 P4 M6 T1 L3 P5 M2 N1",
            "L4 N5 R2 K5 N6"),
            IOStandard("SSTL18_II")),
        Subsignal("ba",    Pins("P2 P3 R1"), IOStandard("SSTL18_II")),
        Subsignal("ras_n", Pins("N4"), IOStandard("SSTL18_II")),
        Subsignal("cas_n", Pins("L1"), IOStandard("SSTL18_II")),
        Subsignal("we_n",  Pins("N2"), IOStandard("SSTL18_II")),
        Subsignal("cs_n",  Pins("K6"), IOStandard("SSTL18_II")),
        Subsignal("dm", Pins("U1 T6"), IOStandard("SSTL18_II")),
        Subsignal("dq", Pins(
            "R7 V6 R8 U7 V7 R6 U6 R5",
            "T5 U3 V5 U4 V4 T4 V1 T3"),
            IOStandard("SSTL18_II"),
            Misc("IN_TERM=UNTUNED_SPLIT_40")),
        Subsignal("dqs_p", Pins("U9 U2"),
            IOStandard("DIFF_SSTL18_II"),
            Misc("IN_TERM=UNTUNED_SPLIT_40")),
        Subsignal("dqs_n", Pins("V9 V2"),
            IOStandard("DIFF_SSTL18_II"),
            Misc("IN_TERM=UNTUNED_SPLIT_40")),
        Subsignal("clk_p", Pins("L6"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("clk_n", Pins("L5"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("cke",   Pins("M1"), IOStandard("SSTL18_II")),
        Subsignal("odt",   Pins("M3"), IOStandard("SSTL18_II")),
        Misc("SLEW=FAST"),
    ),

    # RMII Ethernet
    ("eth_clocks", 0,
        Subsignal("ref_clk", Pins("D5")),
        IOStandard("LVCMOS33"),
    ),

    ("aud_pwm", 0,
        Subsignal("pwm_out", Pins("A11")),
        Subsignal("enable", Pins("D12")),
        IOStandard("LVCMOS33"),
    ),

    ("eth", 0,
        Subsignal("rst_n",   Pins("B3")),
        Subsignal("rx_data", Pins("C11 D10")),
        Subsignal("crs_dv",  Pins("D9")),
        Subsignal("tx_en",   Pins("B9")),
        Subsignal("tx_data", Pins("A10 A8")),
        Subsignal("mdc",     Pins("C9")),
        Subsignal("mdio",    Pins("A9")),
        Subsignal("rx_er",   Pins("C10")),
        Subsignal("int_n",   Pins("B8")),
        IOStandard("LVCMOS33")
     ),

    # VGA
     ("vga", 0,
        Subsignal("hsync_n", Pins("B11")),
        Subsignal("vsync_n", Pins("B12")),
        Subsignal("r", Pins("A3 B4 C5 A4")),
        Subsignal("g", Pins("C6 A5 B6 A6")),
        Subsignal("b", Pins("B7 C7 D7 D8")),
        IOStandard("LVCMOS33")
    ),
]

# Connectors ---------------------------------------------------------------------------------------

_connectors = [
    ("pmoda",    "C17 D18 E18 G17 D17 E17 F18 G18"),
    ("pmodb",    "D14 F16 G16 H14 E16 F13 G13 H16"),
    ("pmodc",    "K1 F6 J2 G6 E7 J3 J4 E6"),
    ("pmodd",    "H4 H1 G1 G3 H2 G4 G2 F3"),
    ("pmodxdac", "A14 A13 A16 A15 B17 B16 A18 B18"),
]

# PMODS --------------------------------------------------------------------------------------------

def sdcard_pmod_io(pmod):
    return [
        # SDCard PMOD:
        # - https://store.digilentinc.com/pmod-microsd-microsd-card-slot/
        ("spisdcard", 0,
            Subsignal("clk",  Pins(f"{pmod}:3")),
            Subsignal("mosi", Pins(f"{pmod}:1"), Misc("PULLUP True")),
            Subsignal("cs_n", Pins(f"{pmod}:0"), Misc("PULLUP True")),
            Subsignal("miso", Pins(f"{pmod}:2"), Misc("PULLUP True")),
            Misc("SLEW=FAST"),
            IOStandard("LVCMOS33"),
        ),
        ("sdcard", 0,
            Subsignal("data", Pins(f"{pmod}:2 {pmod}:4 {pmod}:5 {pmod}:0"), Misc("PULLUP True")),
            Subsignal("cmd",  Pins(f"{pmod}:1"), Misc("PULLUP True")),
            Subsignal("clk",  Pins(f"{pmod}:3")),
            Subsignal("cd",   Pins(f"{pmod}:6")),
            Misc("SLEW=FAST"),
            IOStandard("LVCMOS33"),
        ),
]
_sdcard_pmod_io = sdcard_pmod_io("pmodd") # SDCARD PMOD on JD.

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name   = "clk100"
    default_clk_period = 1e9/100e6

    def __init__(self, variant= "a7-100", toolchain="vivado"):
        device = {
            "a7-50":    "xc7a50t-1csg324i",
            "a7-100":   "xc7a100tcsg324-1"
        }[variant]
        XilinxPlatform.__init__(self, device, _io, _connectors, toolchain=toolchain)
        self.toolchain.bitstream_commands = \
            ["set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]"]
        self.toolchain.additional_commands = \
            ["write_cfgmem -force -format bin -interface spix4 -size 16 "
             "-loadbit \"up 0x0 {build_name}.bit\" -file {build_name}.bin"]        
        self.add_platform_command("set_property INTERNAL_VREF 0.900 [get_iobanks 34]")

    def create_programmer(self):
        bscan_spi = "bscan_spi_xc7a100t.bit" if "xc7a100t" in self.device else "bscan_spi_xc7a50t.bit"
        return OpenOCD("openocd_xc7_ft2232.cfg", bscan_spi)

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk100",             loose=True), 1e9/100e6)
        self.add_period_constraint(self.lookup_request("eth_clocks:ref_clk", loose=True), 1e9/50e6)
