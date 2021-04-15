from song import song


simple_verses = (('verse1 line1', 'verse1 line2'),
                 ('verse2 line1', 'verse2 line2', 'verse2 line3'),
                 ('verse3 line1',))
simple_chorus = ('** CHORUS line1', '** CHORUS line2')
love_verses = (("There's nothing you can do that can't be done",
                "Nothing you can sing that can't be sung",
                'Nothing you can say but you can learn how to play the game',
                "It's easy\n"),
               ("Nothing you can know that isn't known",
                "Nothing you can see that isn't shown",
                "Nowhere you can be that isn't where you're meant to be",
                "It's easy\n"))
love_chorus = ('All you need is love', 'All you need is love',
               'All you need is love, love', 'Love is all you need\n')


def print_test_case(verses, chorus, test_description):
    print('\n' + f'test - {test_description}'.center(40, '_'))
    print('[start]', *song(verses, chorus), '[end]', sep='\n')


if __name__ == '__main__':
    print_test_case(simple_verses, simple_chorus, 'simple')
    print_test_case(love_verses, love_chorus, 'normal song')
    print_test_case((tuple(), ('verse2 line1', 'verse2 line2')),
                    simple_chorus, 'one verse = empty tuple')
    print_test_case(tuple(), simple_chorus, 'verses = empty tuple')
    print_test_case(simple_verses, tuple(), 'chorus = empty tuple')
    print_test_case(tuple(), tuple(), 'both arguments empty')
