<template>
    <div>
        <div class="d-flex flex-column flex-md-row align-items-center p-3 bg-white border-bottom shadow-sm">
            <h5 class="my-0 mr-md-auto font-weight-normal">Ghibli Movies</h5>
        </div>

        <div class="container">
            <div class="row">
                <div class="col">
                    <!-- Show when API Request fails -->
                    <div v-show="axios_error">
                        <div><strong>Error during fetching data</strong></div>
                        <div class="alert alert-danger">
                            {{ axios_error }}
                            <div>
                                Please try again a bit later, if problems will persist contact with
                                developers.
                            </div>
                        </div>
                    </div>
                    <!-- Show when API Request succeed -->
                    <table class="table table-hover table-striped" v-show="!axios_error">
                        <thead>
                            <tr>
                                <th>Movie Title</th>
                                <th>Release Date</th>
                                <th>Ghibli Score</th>
                                <th>Cast</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="movie in movies" :key="movie.id">
                                <td>{{movie.title}}</td>
                                <td align="center">
                                   {{ movie.release_date }}
                                </td>
                                <td align="right">
                                    {{ movie.rt_score }}
                                </td>
                                <td>
                                    <li v-for="person in movie.people" :key="person.id">
                                      {{ person.name }}
                                    </li>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
module.exports = {
    name: 'App',
    data() {
        return {
            movies: null,
            axios_error: null
        }
    },
    mounted() {
        let me = this;

        me.axios_error = null;

        axios
            .get(Urls.movies())
            .then(response => {
                me.movies = response.data.movies;
            })
            .catch(error => {
                me.axios_error = error;
            })
    }
};
</script>