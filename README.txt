YETI MOD for free_ski64
=======================

Two changes:
  (1) Yeti player sprites:  18 BMPs cut pixel-for-pixel from your
      "PC _ Computer - SkiFree - Miscellaneous - Characters.png" sheet
      (Wing Wang Wao rip).
  (2) Source patch:  yeti eats dog/skier/snowboarder on contact and
      scores 1/3/5 style points.

================================================================
1)  SPRITE FILES
================================================================
Files in ./resources/ are drop-in replacements for the placeholder
BMPs in your project. Copy them into:

    <your_project>/resources/

Slot       Source cell from sheet              Mirror   Pose
-------    --------------------------------    ------   --------------------
ski32_5    yeti facing left                    yes      turn slight right
ski32_6    yeti walking right (profile)        no       turn more right
ski32_7    yeti facing right (skinny)          no       facing fully right
ski32_8    yeti standing, arms wide            no       snowplow / brake
ski32_9    yeti standing, arms wide            yes      snowplow (mirror)
ski32_10   yeti arms up                        no       crouch / prep jump
ski32_11   yeti arms up                        no       mid-air
ski32_12   yeti walking (row 2)                no       sitting / fallen
ski32_13   yeti walking (row 2)                yes      crashed (mirror)
ski32_14   yeti rear view                      no       wipeout 1
ski32_15   yeti rear view                      yes      wipeout 2
ski32_16   yeti arms up                        yes      wipeout 3
ski32_17   yeti standing, arms wide            no       wipeout 4
ski32_18   yeti CHOMP red victim               no       eat-frame (was
                                                        "eaten-by-yeti")
ski32_19   yeti carry blue victim              no       roar with prey
ski32_20   yeti facing right                   no       chairlift seated
ski32_21   yeti facing left                    no       chairlift hanging
ski32_22   yeti toss/drop                      no       side carry / final

Each BMP is 32x43, 24-bit, uncompressed Windows BMP. Pure white
(#FFFFFF) is the transparent color, matching SkiFree's convention.
The sprite is centered horizontally; padded edges are white so they
blit transparently.

Slots 1..4 (your existing yeti drawings) are NOT touched.

================================================================
2)  SOURCE PATCH
================================================================
File:  ./skifree_decomp.c   (drop-in replacement for the one in
                             your project root)

Diff summary:  about 30 new lines inserted near line 2284 inside
the collision-handler switch.  Look for the comment banner
"YETI-AS-PLAYER: eat NPCs on contact".

Behavior on collision:
   - ACTOR_TYPE_2_DOG          -> +1 style point, dog is eaten
   - ACTOR_TYPE_1_BEGINNER     -> +3 style points, skier is eaten
   - ACTOR_TYPE_3_SNOWBOARDER  -> +5 style points, snowboarder is eaten
The eaten actor is removed using the same FLAG_8 mechanism the
original yeti uses to remove the player.  Chomp sound (sound_7,
same as the original yeti) plays and the player snaps to the
roar/eat frame (sprite index 0x13 = ski32_19.bmp).

Notes:
  * Points are added directly to `stylePoints` so they always count
    regardless of game mode. To gate them to Freestyle only, swap
    the line  `stylePoints += eatPoints;`
    with     `addStylePoints(eatPoints);`
  * `local_c == 0x11` (already-wiped-out) is preserved — collisions
    are still ignored in that state.

================================================================
3)  REBUILD
================================================================
Open the project in Visual C++ (skifree_decomp.dsp / .dsw) or use
the supplied .mak.  The recompiled skifree_decomp.exe should run
as before, but you'll be the yeti, eating everyone you bump into.

================================================================
4)  TWEAKS YOU MIGHT WANT
================================================================
  * If a particular pose doesn't match what you want, just regenerate
    just that slot:  the sprite sheet PNG is at
    C:\Users\st