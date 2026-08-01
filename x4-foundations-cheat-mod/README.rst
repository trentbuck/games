Take a unique ship (so you have it, and the AI doesn't), and
try to give an interceptor's speed and agility, and
a destroyer's firepower and defense.

I initially wanted to do the Hydra Regal because it looks pretty, and has fewer ramps than the Astrid.
But most of Hydra Regal's components are shared with baseline Hydra.
So instead I'm looking at the Xperimental Shuttle.
As an S-klass ship that can dock in a few more places (e.g. several times early in the Boron questline).
I think the Katana's FPS dashboard and cockpit is cleaner than any of the above, but oh well.

In testing, S- and M-class engines don't get world models, so you can put those on.
Adding L-class engines to an S-class ship works but looks funny because world models.
Adding L-class weapons to an S-class ship also works, but I couldn't get out of the boarding ramp because the ion cannons blocked it.
M-class weapons mostly fit OK to an S-class ship, although some of them will gimbal enough to obscure large parts of your cockpit.

In this initial version, running ALL the diffs against ALL the source XML files is breaking somehow.
When I kill an enemy or (sometimes) when I go through a gate, the whole game hangs.
Next step is to compile the .cat from one-xml-per-dat files that will only edit one file each.
