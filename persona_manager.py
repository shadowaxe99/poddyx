import json

def set_persona(persona: str):
    # Logic to set persona
    pass


def get_persona() -> str:
    # Logic to get current persona
    pass


def main():
    persona = get_persona()
    while True:
        user_input = input()
        if user_input.startswith("INTERRUPT:"):
            interrupt = user_input.split(":", 1)[1]
            handle_interrupts(interrupt)
        elif user_input.startswith("SET PERSONA:"):
            new_persona = user_input.split(":", 1)[1]
            set_persona(new_persona)
        else:
            handle_dialog(user_input)


if __name__ == "__main__":
    main()
