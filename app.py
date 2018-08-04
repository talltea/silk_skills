import click
from skill_storage import FileStorage

skill_storage = FileStorage('temp.json')

@click.command()
def main():
    """For testing stuff I guess"""
    skills = skill_storage.list_skills()
    click.echo(skill_storage.list_skills())

    skills.append({'test':55})
    skill_storage._overwrite_skills(skills)
    click.echo(skill_storage.list_skills())

    new_skill = {"I'm new!": "hi"}
    skill_storage.add_skill(new_skill)
    click.echo(skill_storage.list_skills())

if __name__ == '__main__':
    main()
