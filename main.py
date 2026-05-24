import subprocess
import sys
import os
from pathlib import Path
from groq import Groq
from rich.console import Console
from rich.panel import Panel

console = Console()

# We save the key securely in the user's home directory
CONFIG_FILE = Path.home() / ".savage_commit_key"

def get_api_key():
    # Check if the key is already saved
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            return f.read().strip()
    
    # If not, ask the user for it (First time setup)
    console.print(Panel("[bold red]🔥 Savage-Commit Initial Setup[/bold red]\n\n"
                        "To keep this tool 100% free, it uses your own Groq API Key.\n"
                        "Get yours for free at: [blue]https://console.groq.com/keys[/blue]"))
    
    key = console.input("[bold yellow]Paste your Groq API Key: [/bold yellow]").strip()
    
    # Save it so they don't have to enter it again
    with open(CONFIG_FILE, "w") as f:
        f.write(key)
    
    console.print("[bold green]✅ Key saved securely! Let's judge your code...[/bold green]\n")
    return key

def get_git_diff():
    try:
        subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], check=True, capture_output=True)
        diff = subprocess.check_output(['git', 'diff', '--staged'], encoding='utf-8')
        return diff
    except subprocess.CalledProcessError:
        console.print("[bold red]❌ Error: You are not in a Git repository![/bold red]")
        sys.exit(1)

def generate_commit_and_roast(diff, api_key):
    client = Groq(api_key=api_key)
    
    prompt = f"""
    You are a sarcastic, highly experienced senior developer.
    Analyze this git diff:
    {diff}
    
    Provide:
    1. COMMIT: A professional commit message (conventional commits).
    2. ROAST: A brutal, funny, 1-sentence roast of the code.
    
    Format:
    COMMIT: [message]
    ROAST: [roast]
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    diff = get_git_diff()
    
    if not diff.strip():
        console.print("[bold yellow]📂 No changes staged. Run 'git add .' first![/bold yellow]")
        sys.exit(0)
        
    api_key = get_api_key()
    
    with console.status("[bold cyan]🚀 Senior Dev is judging your code...[/bold cyan]", spinner="dots"):
        try:
            result = generate_commit_and_roast(diff, api_key)
            
            # Split the response to colorize them differently
            parts = result.split("ROAST:")
            commit_msg = parts[0].replace("COMMIT:", "").strip()
            roast_msg = parts[1].strip() if len(parts) > 1 else "No roast today."
            
            # Print Beautiful Panels
            console.print(Panel(f"[bold green]{commit_msg}[/bold green]", title="[bold white]✨ Suggested Commit[/bold white]"))
            console.print(Panel(f"[bold red]{roast_msg}[/bold red]", title="[bold white]🔥 Senior Dev Roast[/bold white]"))
            
        except Exception as e:
            console.print(f"[bold red]❌ Error: {e}[/bold red]")
            # If the key is invalid, delete the config file so they can try again
            if "Authentication" in str(e) or "401" in str(e):
                CONFIG_FILE.unlink(missing_ok=True)