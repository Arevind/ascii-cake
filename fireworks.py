#!/usr/bin/env python3
"""
Birthday CLI App - A personalized birthday greeting with ASCII art, music, and scrolling letter
"""
import os
import time
import sys
import threading
import random
from pathlib import Path

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False
    print("Note: pygame not installed. Music playback will be simulated.")

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.live import Live
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt

console = Console()

# ASCII Art (using raw strings to preserve backslashes)
ASCII_ART = [
    r"       .                      .    *+*+*   +             *       .---,    ",
    r"               }       *           |||||       .---.            /#    `\  ",
    r"     .--.     {            )     @@.@.@.@@    /     \  .        |      |  ",
    r"    /    \     }          (      |'='='='|    |#     |          '.   _/   ",
    r"    |#   |         +            @@.@.@.@.@@   '._ _,/             `(^     ",
    r"    \_ _.'   +          *   )   |'='='='='|     (^            +     )     ",
    r"     (^   *       .            @@.@.@.@.@.@@     )        *        (      ",
    r"      )  _ _  ___  ___  ___+__  __  ___  _  ___  ___+ _ _  ___  ___ __ *__",
    r"     (  | | |/   \|   \|   \\ \/ / | _ \| ||   \|   || | ||   \/   \\ \/ /",
    r"      ) |   || - || -_/| -_/ \  /  | _ <| || - / | | |   || | || - | \  / ",
    r"        |_|_||_|_||_|  |_|   /_/   |___/|_||_._\ |_| |_|_||___/|_|_| /_/  "
]

BIRTHDAY_LETTER = """
Dear Unknown person,
                    I know you are unknown😅, but you are the most valuable person to me, I wish you the Happiest of Birthdays!🎂

With best wishes,
the dude who spent too much time making this.
"""

class MusicPlayer:
    def __init__(self):
        self.playing = False
        self.music_thread = None
    
    def play_music(self, filename="music.mp3"):
        # Music by
        #https://pixabay.com/users/pianocafe_kumi-35185506/
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
            
        music_path = os.path.join(base_path, filename)

        if PYGAME_AVAILABLE:
            try:
                if not Path(music_path).exists():
                    console.print(f"❌ Music file '{music_path}' not found.", style="red")
                    self._simulate_music()
                    return
                
                pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
                pygame.mixer.init()
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.playing = True
                console.print(f"🎵 Successfully playing: {filename}", style="bright_green")
                
            except pygame.error as e:
                console.print(f"❌ Pygame error: {e}", style="red")
                self._simulate_music()
            except Exception as e:
                console.print(f"❌ Unexpected error playing music: {e}", style="red")
                self._simulate_music()
        else:
            console.print("❌ Pygame not available. Installing pygame might fix this:", style="red")
            console.print("   pip install pygame", style="bright_cyan")
            self._simulate_music()
    
    def _simulate_music(self):
        """Simulate music playback with a visual indicator"""
        self.playing = True
        console.print("🎵 ♪♫♪ Music simulation mode - No actual audio playing ♪♫♪", style="bright_magenta")
    
    def stop_music(self):
        """Stop the music"""
        if self.playing and PYGAME_AVAILABLE:
            try:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
            except:
                pass
        self.playing = False
        console.print("🎵 Music stopped", style="dim")

class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.colors = [
            "bright_red", "bright_green", "bright_blue", "bright_yellow", 
            "bright_magenta", "bright_cyan", "bright_white", "red", 
            "green", "blue", "yellow", "magenta", "cyan"
        ]
        self.exploded = False
        self.launch_height = random.randint(8, 15)
        self.current_height = 25
        
    def launch(self):
        """Launch phase - rocket going up"""
        if self.current_height > self.launch_height:
            self.current_height -= 1
            return f"{'':>{self.x}}{'|' if random.random() > 0.5 else '^'}"
        else:
            self.exploded = True
            self.create_explosion()
            return ""
    
    def create_explosion(self):
        """Create explosion particles"""
        num_particles = random.randint(15, 25)
        for _ in range(num_particles):
            angle = random.uniform(0, 360)
            speed = random.uniform(2, 6)
            color = random.choice(self.colors)
            
            import math
            vel_x = speed * math.cos(math.radians(angle))
            vel_y = speed * math.sin(math.radians(angle))
            
            particle = {
                'x': self.x,
                'y': self.current_height,
                'vel_x': vel_x,
                'vel_y': vel_y,
                'color': color,
                'life': random.randint(8, 15),
                'char': random.choice(['*', '✦', '✧', '❋', '✪', '●', '◆', '♦'])
            }
            self.particles.append(particle)
    
    def update(self):
        """Update explosion particles"""
        if not self.exploded:
            return [self.launch()]
        
        lines = [""] * 30
        active_particles = []
        
        for particle in self.particles:
            if particle['life'] > 0:
                # Update position
                particle['x'] += particle['vel_x'] / 4
                particle['y'] += particle['vel_y'] / 4
                particle['vel_y'] += 0.3  
                particle['life'] -= 1
                
                x_pos = int(particle['x'])
                y_pos = int(particle['y'])
                
                if 0 <= x_pos < 120 and 0 <= y_pos < 30:
                    if not lines[y_pos]:
                        lines[y_pos] = " " * 120
                    
                    line_list = list(lines[y_pos])
                    if x_pos < len(line_list):
                        line_list[x_pos] = particle['char']
                        lines[y_pos] = ''.join(line_list)
                
                active_particles.append(particle)
        
        self.particles = active_particles
        return lines

def show_fireworks_animation():
    """Display a beautiful 3-second firework animation"""
    console.clear()
    
    fireworks = []
    animation_frames = []
    firework_timings = [
        (10, [20, 40, 60, 80]),  
        (25, [30, 70]),          
        (40, [15, 45, 75, 95]),  
        (55, [35, 65]),          
    ]
    
    total_frames = 90 
    
    with Live(console=console, refresh_per_second=30, transient=False) as live:
        for frame in range(total_frames):
            for timing, positions in firework_timings:
                if frame == timing:
                    for pos in positions:
                        fireworks.append(Firework(pos, 25))
            display_lines = [" " * 120 for _ in range(30)]
            
            # Update all fireworks
            for firework in fireworks[:]:
                lines = firework.update()
                

                for i, line in enumerate(lines):
                    if line and i < len(display_lines):
                        combined = ""
                        for j in range(min(len(line), len(display_lines[i]), 120)):
                            if line[j] != ' ' and line[j] != '':
                                combined += line[j]
                            elif display_lines[i][j] != ' ':
                                combined += display_lines[i][j]
                            else:
                                combined += ' '
                        
                        combined += ' ' * (120 - len(combined))
                        display_lines[i] = combined[:120]
                
                if firework.exploded and not firework.particles:
                    fireworks.remove(firework)

            display_text = Text()
            
            # Add title
            if frame < 30:
                title_text = "🎆 BIRTHDAY FIREWORKS SPECTACULAR! 🎆"
            elif frame < 60:
                title_text = "✨ CELEBRATING YOU! ✨"
            else:
                title_text = "🎉 LET THE CELEBRATION BEGIN! 🎉"
            
            display_text.append(f"{title_text:^120}\n", style="bold bright_yellow")
            display_text.append("\n")
            
            for line in display_lines:
                colored_line = Text()
                for char in line:
                    if char in ['*', '✦', '✧', '❋', '✪', '●', '◆', '♦']:
                        color = random.choice([
                            "bright_red", "bright_green", "bright_blue", 
                            "bright_yellow", "bright_magenta", "bright_cyan"
                        ])
                        colored_line.append(char, style=color)
                    elif char in ['|', '^']:
                        colored_line.append(char, style="bright_white")
                    else:
                        colored_line.append(char, style="dim")
                
                display_text.append(colored_line)
                display_text.append("\n")
            
            # Add bottom message
            if frame > 60:
                bottom_msg = "🎈 Get ready for your special message! 🎈"
                display_text.append(f"\n{bottom_msg:^120}", style="bold bright_magenta")
            
            live.update(display_text)
            time.sleep(0.033)  # ~30fps
    console.clear()
    time.sleep(1)

def run_fake_scripts():
    """Runs a series of fake loading and access scripts."""
    console.clear()
    
    script_steps = [
        ("[bright_yellow]Loading essential scripts...", 1),
        ("[bright_green]Scripts have been successfully initialized.", 1.5),
        ("[bright_yellow]Loading data on target...", 1),
        ("[bright_red]DATA Loading failed. Connection timed out.", 1.5),
        ("[bright_red]Unauthorized Access Detected.", 1),
        ("[bright_cyan]Authorization required. Running user verification protocol...", 1.5)
    ]

    for step, sleep_time in script_steps:
        console.print(f"[bold]{step}[/bold]")
        time.sleep(sleep_time)


def run_verification_quiz():
    """Runs the user verification quiz."""
    console.clear()
    console.print(Panel(Align.center(Text("🔐 Verification Quiz 🔐", style="bold bright_yellow")), style="bright_cyan"))
    console.print()
    
    while True:
        proceed = Prompt.ask(
            Text("Access is unauthorized. Do you wish to proceed with verification?", style="bold bright_magenta"),
            choices=["Y", "N"],
            default="Y"
        ).lower()
        
        if proceed == 'n':
            console.print(Panel(Align.center("Access Denied."), style="red"))
            console.print("Program will now exit.", style="dim")
            sys.exit(0)
        
        if proceed == 'y':
            break

    # Question 1
    answer1 = Prompt.ask(
        "Weird question No.1 ? (Reply 'ok')",
        console=console
    ).lower()
    if answer1 == "ok":
        console.print(Panel(Align.center("Step 1/3: Successful"), style="green"))
        time.sleep(1)
    else:
        show_intruder_screen()
    
    # Question 2
    answer2 = Prompt.ask(
        "   Weirder question No.2 ? (Reply 'ookk')",
        console=console
    ).lower()
    if answer2 == "ookk":
        console.print(Panel(Align.center("Step 2/3: Successful"), style="green"))
        time.sleep(1)
    else:
        show_intruder_screen()
    
    # Question 3
    answer3 = Prompt.ask(
        "Who is the coolest of them all ? (Reply 'Arevind')",
        console=console
    ).lower()
    if answer3 == "arevind":
        console.print(Panel(Align.center("Step 3/3: Successful \n Affirmative. Your response has been cross-referenced with the primary data source and has yielded an outcome of profound satisfaction for the program's architect."), style="green"))
        time.sleep(5)
    else:
        show_intruder_screen()

def show_intruder_screen():
    """Simulates a data wipe and exits."""
    console.clear()
    console.print(Panel(Align.center(Text("🚨 INTRUDER DETECTED 🚨", style="bold bright_red")), style="red"))
    console.print(Align.center("Force closing program..."), style="dim")
    console.print()
    
    script_steps = [
        ("[bright_red]Data wipe initialized.", 1),
        ("[red]Terminating all processes...", 1),
        ("[dim]Deleting temporary files...", 1),
        ("[dim]Shutting down system...", 1)
    ]
    
    for step, sleep_time in script_steps:
        console.print(f"[bold]{step}[/bold]")
        time.sleep(sleep_time)

    sys.exit(1)

def show_loading_screen():
    """Show a beautiful loading screen"""
    console.clear()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("[bright_magenta]Preparing the celebratory data matrix...", total=100)
        
        for i in range(100):
            progress.update(task, advance=1)
            time.sleep(0.03)

def display_ascii_art():
    """Display the ASCII art with beautiful styling"""
    console.clear()
    
    title = Text("MESSAGE TRANSMISSION FROM AN AI INTERN TO A CS-AI STUDENT", style="bold bright_yellow")
    title_panel = Panel(
        Align.center(title),
        box=box.DOUBLE,
        style="bright_magenta",
        padding=(1, 2)
    )
    
    console.print(title_panel)
    console.print()
    
    art_text = Text()
    colors = ["bright_cyan", "cyan", "bright_blue", "blue", "bright_magenta", "magenta", "bright_red", "red", "bright_yellow", "yellow", "bright_green"]
    
    for i, line in enumerate(ASCII_ART):
        color = colors[i % len(colors)]
        art_text.append(line + "\n", style=color)
    
    art_panel = Panel(
        Align.center(art_text),
        box=box.HEAVY,
        style="bright_white",
        title="COMMEMORATIVE VISUALS PROTOCOL",
        title_align="center"
    )
    
    console.print(art_panel)
    console.print()

def scroll_letter(letter_text, delay=0.5):
    """Scroll through the birthday letter smoothly"""
    console.clear()
    
    letter_panel_title = Text("💌 A Special Message Just For You 💌", style="bold bright_yellow")
    console.print(Panel(Align.center(letter_panel_title), style="magenta"))
    console.print()
    
    paragraphs = letter_text.strip().split('\n\n')
    
    for i, paragraph in enumerate(paragraphs):
        if i > 0:
            time.sleep(delay)  # Pause between paragraphs
        
        console.clear()
        console.print(Panel(Align.center(letter_panel_title), style="magenta"))
        console.print()
        
        for j in range(i + 1):
            panel = Panel(
                paragraphs[j],
                box=box.ROUNDED,
            
                style="bright_cyan",
                padding=(1, 2)
            )
            console.print(panel)
            console.print()
    
    time.sleep(5)

def show_finale():
    """Show a beautiful finale screen"""
    console.print()
    console.print()
    
    finale_text = Text()
    finale_text.append("🎉 ", style="bright_yellow")
    finale_text.append("Hope your special day is absolutely wonderful!", style="bold bright_magenta")
    finale_text.append(" 🎉", style="bright_yellow")
    
    finale_panel = Panel(
        Align.center(finale_text),
        box=box.DOUBLE,
        style="bright_green",
        padding=(2, 4)
    )
    
    console.print(finale_panel)
    
    wishes = ["🎂", "🎈", "🎁", "✨", "🌟", "💖", "🎊", "🥳"]
    wish_line = Text()
    
    for wish in wishes:
        wish_line.append(f"{wish} ", style="bright_yellow")
        time.sleep(0.2)
        console.print(Align.center(wish_line), end="\r")
    
    console.print()
    console.print()

def main():
    """Main function to run the birthday app"""
    music_player = MusicPlayer()
    
    try:
        run_fake_scripts()
        run_verification_quiz()
        
        show_loading_screen()
        
        music_player.play_music("music.mp3")         
        show_fireworks_animation()
        
        display_ascii_art()
        
        console.print(Align.center(
            Text("Press Enter to initiate data decryption and review the transmission...", style="bold bright_green")
        ))
        input()
        
        scroll_letter(BIRTHDAY_LETTER)
        
        show_finale()
        
        console.print(Align.center(
            Text("Press Enter to exit or 'r' + Enter to replay...", style="dim bright_white")
        ))
        
        choice = input().lower().strip()
        if choice == 'r':
            main()  # Replay
        
    except KeyboardInterrupt:
        console.print("\n\n🎈 Thanks for celebrating! 🎈", style="bright_yellow")
    
    finally:
        music_player.stop_music()

if __name__ == "__main__":
    try:
        from rich.console import Console
    except ImportError:
        print("Please install the 'rich' library: pip install rich")
        sys.exit(1)
    
    console.print(
        Panel(
            Align.center(Text("COMMENCING HIGH-PRIORITY DATA TRANSFER AND VISUALIZATION PROTOCOL...", style="bold bright_magenta")),
            style="bright_cyan"
        )
    )
    time.sleep(1)
    
    main()